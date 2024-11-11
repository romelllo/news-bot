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
        business = "business"
        general = "general"
        health = "health"
        science = "science"
        technology = "technology"

    # class NewsApiSources(str, Enum):

    def newsapi_categories_to_track_values_list(self):
        return list(category.value for category in self.NewsApiCategoriesToTrack)

    def newsapi_top_headlines_url(self):
        return urljoin(self.NEWSAPI_BASE_URL + '/', self.NEWSAPI_TOP_HEADLINES_ENDPOINT)

    def newsapi_sources_url(self):
        return urljoin(self.newsapi_top_headlines_url() + '/', self.NEWSAPI_SOURCES_ENDPOINT)
    
    def newsapi_sources_url_lang(self):
        return f"{self.newsapi_sources_url()}?language={self.NEWSAPI_DEFAULT_LANGUAGE}"
    
    def newsapi_sources_url_lang_country(self):
        return f"{self.newsapi_sources_url_lang()}&country={self.NEWSAPI_DEFAULT_COUNTRY}"
    
    def newsapi_sources_url_lang_country_category(self, category: str):
        return f"{self.newsapi_sources_url_lang_country()}&category={category}"
    

settings = Settings()
