from dataclasses import dataclass


@dataclass
class NewsApiSourceSettings:
    api_key: str
    base_url: str = 'https://newsapi.org/v2/'
    sources_endpoint: str = 'sources'
    top_headlines_endpoint: str = 'top-headlines'
    everything_endpoint: str = 'everything'
    country: str = 'us'
    # TODO: Add more settings for sources