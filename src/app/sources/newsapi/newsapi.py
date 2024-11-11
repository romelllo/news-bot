import asyncio

import httpx

from src.app.sources.newsapi.settings import settings
from src.app.utils import with_retry

HEADERS = {"X-Api-Key": settings.NEWSAPI_KEY}

@with_retry()
async def get_response_json(url: str) -> dict:
    async with httpx.AsyncClient(headers=HEADERS) as client:
        response = await client.get(url)
        return response.json()


async def main():
    categories = settings.newsapi_categories_to_track_values_list()

    sources = []
    for category in categories:
        newsapi_sources = await get_response_json(settings.newsapi_sources_url_lang_country_category(category))
        sources.extend(source['id'] for source in newsapi_sources['sources'])

    print(sources)


if __name__ == "__main__":
    asyncio.run(main())
