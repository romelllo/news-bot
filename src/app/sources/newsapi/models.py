from typing import Optional

from pydantic import BaseModel, HttpUrl

from src.app.sources.newsapi.settings import settings


class Source(BaseModel):
    id: settings.NewsApiSourcesToTrackIds
    name: settings.NewsApiSourcesToTrackNames


class ArticleIn(BaseModel):
    source: Source
    author: Optional[str]
    title: str
    description: Optional[str]
    url: HttpUrl
    urlToImage: Optional[HttpUrl]
    publishedAt: str
    content: str


class ArticleOut(BaseModel):
    source: settings.NewsApiSourcesToTrackIds
    title: str
    description: Optional[str]
    content: str
