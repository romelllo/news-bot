from enum import Enum
from urllib.parse import urljoin

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NEWSAPI_KEY: str
    NEWSAPI_BASE_URL: str = "https://newsapi.org/v2"
    NEWSAPI_TOP_HEADLINES_ENDPOINT: str = "top-headlines"
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

    class NewsApiSourcesToTrack(str, Enum):
        REUTERS = "reuters"
        MEDICAL_NEWS_TODAY = "medical-news-today"
        NEW_SCIENTIST = "new-scientist"
        ARS_TECHNICA = "ars-technica"
        CRYPTO_COIN_NEWS = "crypto-coins-news"
        ENGADGET = "engadget"
        HACKER_NEWS = "hacker-news"
        TECHCRUNCH = "techcrunch"
        THE_VERGE = "the-verge"
        WIRED = "wired"

    def newsapi_categories_to_track_values_list(self):
        return list(category.value for category in self.NewsApiCategoriesToTrack)
    
    def newsapi_sources_to_track_values_list(self):
        return list(source.value for source in self.NewsApiSourcesToTrack)

    def newsapi_top_headlines_url(self):
        return urljoin(self.NEWSAPI_BASE_URL + '/', self.NEWSAPI_TOP_HEADLINES_ENDPOINT)
    
    def news_api_top_headlines_url_sources(self, sources: str):
        return f"{self.newsapi_top_headlines_url()}?sources={sources}"

    def newsapi_sources_url(self):
        return urljoin(self.newsapi_top_headlines_url() + '/', self.NEWSAPI_SOURCES_ENDPOINT)
    
    def newsapi_sources_url_lang(self):
        return f"{self.newsapi_sources_url()}?language={self.NEWSAPI_DEFAULT_LANGUAGE}"
    
    def newsapi_sources_url_lang_country(self):
        return f"{self.newsapi_sources_url_lang()}&country={self.NEWSAPI_DEFAULT_COUNTRY}"
    
    def newsapi_sources_url_lang_category(self, category: str):
        return f"{self.newsapi_sources_url_lang()}&category={category}"
    
    def newsapi_sources_url_lang_country_category(self, category: str):
        return f"{self.newsapi_sources_url_lang_country()}&category={category}"
    

settings = Settings()
