from enum import Enum
from urllib.parse import urljoin

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NEWSAPI_KEY: str
    NEWSAPI_BASE_URL: str = "https://newsapi.org/v2"
    NEWSAPI_TOP_HEADLINES_ENDPOINT: str = "top-headlines"
    NEWSAPI_EVERYTHING_ENDPOINT: str = "everything"
    NEWSAPI_SOURCES_ENDPOINT: str = "sources"
    NEWSAPI_DEFAULT_LANGUAGE: str = "en"
    NEWSAPI_DEFAULT_COUNTRY: str = "us"

    class Config:
        env_file = ".env"
        extra = "ignore"

    class NewsApiCategoriesToTrack(str, Enum):
        BUSINESS = "business"
        GENERAL = "general"
        HEALTH = "health"
        SCIENCE = "science"
        TECHNOLOGY = "technology"

    class NewsApiSourcesToTrackTopHeadlinesEndpoint(str, Enum):
        REUTERS = "reuters"
        MEDICAL_NEWS_TODAY = "medical-news-today"
        CRYPTO_COIN_NEWS = "crypto-coins-news"
        THE_VERGE = "the-verge"
        WIRED = "wired"

    class NewsApiSourcesToTrackEverythingEndpoint(str, Enum):
        HACKER_NEWS = "hacker-news"
        TECHCRUNCH = "techcrunch"

    class NewsApiSourcesToTrackIds(str, Enum):
        REUTERS = "reuters"
        MEDICAL_NEWS_TODAY = "medical-news-today"
        CRYPTO_COIN_NEWS = "crypto-coins-news"
        THE_VERGE = "the-verge"
        WIRED = "wired"
        HACKER_NEWS = "hacker-news"
        TECHCRUNCH = "techcrunch"

    class NewsApiSourcesToTrackNames(str, Enum):
        REUTERS = "Reuters"
        MEDICAL_NEWS_TODAY = "Medical News Today"
        CRYPTO_COIN_NEWS = "Crypto Coins News"
        THE_VERGE = "The Verge"
        WIRED = "Wired"
        HACKER_NEWS = "Hacker News"
        TECHCRUNCH = "TechCrunch"

    def newsapi_categories_to_track_values_list(self):
        return list(category.value for category in self.NewsApiCategoriesToTrack)

    def newsapi_sources_to_track_top_headlines_values_list(self):
        return list(
            source.value for source in self.NewsApiSourcesToTrackTopHeadlinesEndpoint
        )

    def newsapi_sources_to_track_everything_values_list(self):
        return list(
            source.value for source in self.NewsApiSourcesToTrackEverythingEndpoint
        )

    def newsapi_top_headlines_url(self):
        return urljoin(self.NEWSAPI_BASE_URL + "/", self.NEWSAPI_TOP_HEADLINES_ENDPOINT)

    def newsapi_everything_url(self):
        return urljoin(self.NEWSAPI_BASE_URL + "/", self.NEWSAPI_EVERYTHING_ENDPOINT)

    def newsapi_top_headlines_url_sources(self, sources: str):
        return (
            f"{self.newsapi_top_headlines_url()}?sources={sources}&pageSize=100&page=1"
        )

    def newsapi_everything_url_sources(
        self, sources: str, from_date: str, to_date: str
    ):
        return f"{self.newsapi_everything_url()}?sources={sources}&from={from_date}&to={to_date}&sortBy=puplishedAt&pageSize=100&page=1"


settings = Settings()
