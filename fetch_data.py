from newsapi import NewsApiClient
from api import key
import pandas as pd
import datetime as dt
from typing import Dict, List, Any
import os
import logging
import time
your_api_key_here = key

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class NewsCollector:
    def __init__(self, api_key: str):
        """Initialize NewsAPI client with API key"""
        self.newsapi = NewsApiClient(api_key=api_key)
        self.article_limit = 100
        
    def process_article(self, article: Dict) -> Dict:
        """Process a single article and extract relevant fields"""
        return {
            'source_id': article['source'].get('id', ''),
            'source_name': article['source'].get('name', ''),
            'author': article.get('author', ''),
            'title': article.get('title', ''),
            'description': article.get('description', ''),
            'url': article.get('url', ''),
            'urlToImage': article.get('urlToImage', ''),
            'publishedAt': pd.to_datetime(article.get('publishedAt')),
            'content': article.get('content', '')
        }

    def fetch_articles(self, query: str) -> pd.DataFrame:
        """Fetch articles with error handling and rate limiting"""
        try:
            end_date = dt.datetime.now()
            start_date = end_date - dt.timedelta(days=7)
            
            logger.info(f"Fetching articles for query: {query}")
            
            response = self.newsapi.get_everything(
                q=query,
                from_param=start_date.strftime('%Y-%m-%d'),
                to=end_date.strftime('%Y-%m-%d'),
                language='en',
                sort_by='relevancy',
                page_size=self.article_limit
            )
            
            if not response or 'articles' not in response:
                logger.error("No articles found in response")
                return pd.DataFrame()
            
            processed_articles = []
            for article in response['articles'][:self.article_limit]:
                processed_articles.append(self.process_article(article))
            
            # Create DataFrame with specific column order
            df = pd.DataFrame(processed_articles)
            
            # Reorder columns to match required format
            columns_order = [
                'source_id',
                'source_name',
                'author',
                'title',
                'description',
                'url',
                'urlToImage',
                'publishedAt',
                'content'
            ]
            
            df = df[columns_order]
            
            # Add index column that will become 'Unnamed: 0' when saved to CSV
            df.index.name = 'Unnamed: 0'
            
            logger.info(f"Successfully collected {len(df)} articles")
            return df
            
        except Exception as e:
            logger.error(f"Error fetching articles: {str(e)}")
            return pd.DataFrame()

    def save_articles(self, df: pd.DataFrame, query: str) -> None:
        """Save articles to CSV with date in filename"""
        if df.empty:
            logger.warning("No articles to save")
            return
        
        date_str = dt.datetime.now().strftime('%Y%m%d')
        filename = f"{query}_{date_str}.csv"
        
        # Save to CSV with index to create the 'Unnamed: 0' column
        df.to_csv(filename)
        logger.info(f"Saved {len(df)} articles to {filename}")
        
        self.print_data_quality_report(df)

    def print_data_quality_report(self, df: pd.DataFrame) -> None:
        """Print data quality statistics"""
        print("\nData Quality Report:")
        print(f"Total articles: {len(df)}")
        for column in df.columns:
            print(f"Missing {column}: {df[column].isna().sum()}")
        print("\nDate range:")
        print(f"Earliest article: {df['publishedAt'].min()}")
        print(f"Latest article: {df['publishedAt'].max()}")

def main():
    API_KEY = your_api_key_here
    
    # Initialize collector
    collector = NewsCollector(API_KEY)
    
    # Define search query
    query = "deepseek"  # or any other topic you're interested in
    
    # Fetch and save articles
    df = collector.fetch_articles(query)
    collector.save_articles(df, query)

if __name__ == "__main__":
    main()