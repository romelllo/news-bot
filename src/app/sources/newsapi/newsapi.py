import asyncio

import httpx

from src.app.settings import settings

HEADERS = {"X-Api-Key": settings.NEWSAPI_KEY}


async def get_response_json(url: str) -> dict:
    async with httpx.AsyncClient(headers=HEADERS) as client:
        response = await client.get(url)
        return response.json()


async def get_top_headlines_by_country_topic(country: str, category: str) -> dict:
    url = f"{settings.NEWSAPI_BASE_URL}/top-headlines?country={country}&category={category}"
    return await get_response_json(url)
    

async def get_available_sources() -> dict:
    url = f"{settings.NEWSAPI_BASE_URL}/top-headlines/sources"
    return await get_response_json(url)


def get_sources_list_by_language_category(sources_response: dict, language: str, category: list) -> list:
    sources_list = []

    for source in sources_response['sources']:
        if source["language"] == language and source["category"] in category:
            sources_list.append({"name": source["name"], "description": source["description"]})

    return sources_list



async def main():
    country = "us"
    category = ["technology", "science"]
    sources = ["techcrunch", "the-verge"]
    response = await get_available_sources()
    sources_list = get_sources_list_by_language_category(response, "en", category)
    for source in sources_list:
        print(source)


if __name__ == "__main__":
    asyncio.run(main())
