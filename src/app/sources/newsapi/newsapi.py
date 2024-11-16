import asyncio
import json
import logging
from datetime import datetime, timedelta

from src.app.sources.newsapi.models import ArticleIn, ArticleOut
from src.app.sources.newsapi.settings import settings
from src.app.utils import get_response_json

logger = logging.getLogger(__name__)

HEADERS = {"X-Api-Key": settings.NEWSAPI_KEY}


def get_dates() -> tuple[str, str]:
    today = datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

    return yesterday, today


def get_sources() -> tuple[list[str], list[str]]:
    top_headlines_sources = (
        settings.newsapi_sources_to_track_top_headlines_values_list()
    )
    everything_sources = settings.newsapi_sources_to_track_everything_values_list()

    return top_headlines_sources, everything_sources


def get_top_headlines_url(sources) -> str:
    top_headlines_url = settings.newsapi_top_headlines_url_sources(",".join(sources))

    return top_headlines_url


def get_everything_url(sources, yesterday, today) -> str:
    everything_url = settings.newsapi_everything_url_sources(
        ",".join(sources),
        yesterday,
        today,
    )

    return everything_url


def get_filtered_top_headlines_response_based_on_published_at_articles(
    response: dict[str, str | list[dict]],
    date: str,
) -> list[dict]:
    articles = response["articles"]
    return [article for article in articles if article["publishedAt"] >= date]


def get_everything_articles(
    response: dict[str, str | list[dict]],
) -> list[dict]:
    articles = response["articles"]
    return articles


def get_non_empty_articles(articles: list[dict]) -> list[dict]:
    return [article for article in articles if article["content"]]


def prepare_article_out(article: ArticleIn) -> ArticleOut:
    return ArticleOut(
        source=article.source.id,
        title=article.title,
        description=article.description,
        content=article.content,
    )

def save_articles_to_json(articles: list[ArticleOut], filename: str):
    with open(filename, "w") as f:
        json.dump([article.model_dump() for article in articles], f)


async def main():
    yesterday, today = get_dates()

    top_headlines_sources, everything_sources = get_sources()

    top_headlines_url = get_top_headlines_url(top_headlines_sources)
    everything_url = get_everything_url(everything_sources, yesterday, today)

    top_headlines_response = await get_response_json(top_headlines_url, HEADERS)
    everything_response = await get_response_json(everything_url, HEADERS)

    top_headlines_response = (
        get_filtered_top_headlines_response_based_on_published_at_articles(
            top_headlines_response, yesterday
        )
    )

    everything_response = get_everything_articles(everything_response)

    articles = get_non_empty_articles(top_headlines_response + everything_response)
    articles = [ArticleIn(**article) for article in articles]
    articles = [prepare_article_out(article) for article in articles]

    # save_articles_to_json(articles, f"newsapi_{today}.json")


if __name__ == "__main__":
    asyncio.run(main())
