import asyncio
import logging

from src.app.sources.newsapi.settings import settings
from src.app.utils import get_response_json

logger = logging.getLogger(__name__)

HEADERS = {"X-Api-Key": settings.NEWSAPI_KEY}

async def main():
    sources = settings.newsapi_sources_to_track_values_list()

    response = await get_response_json(settings.news_api_top_headlines_url_sources(','.join(sources)), HEADERS)

    print(len(response['articles']))


if __name__ == "__main__":
    asyncio.run(main())
