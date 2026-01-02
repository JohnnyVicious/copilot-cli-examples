"""
Complete Example: Simple Web Scraper
This example demonstrates web scraping with error handling and data extraction.
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class WebScraper:
    """Simple web scraper with common operations."""
    
    def __init__(self, base_url: str, delay: float = 1.0):
        """
        Initialize web scraper
        
        Args:
            base_url: Base URL for scraping
            delay: Delay between requests in seconds
        """
        self.base_url = base_url
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def fetch_page(self, url: str) -> BeautifulSoup:
        """
        Fetch and parse a web page
        
        Args:
            url: URL to fetch
        
        Returns:
            BeautifulSoup object
        """
        try:
            logger.info(f"Fetching {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            time.sleep(self.delay)  # Be respectful to servers
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            raise
    
    def extract_links(self, soup: BeautifulSoup) -> List[str]:
        """
        Extract all links from a page
        
        Args:
            soup: BeautifulSoup object
        
        Returns:
            List of URLs
        """
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('http'):
                links.append(href)
            elif href.startswith('/'):
                links.append(f"{self.base_url}{href}")
        return links
    
    def extract_text(self, soup: BeautifulSoup, selector: str) -> List[str]:
        """
        Extract text from elements matching selector
        
        Args:
            soup: BeautifulSoup object
            selector: CSS selector
        
        Returns:
            List of text content
        """
        elements = soup.select(selector)
        return [elem.get_text(strip=True) for elem in elements]
    
    def extract_table(self, soup: BeautifulSoup, table_id: str = None) -> List[Dict]:
        """
        Extract table data
        
        Args:
            soup: BeautifulSoup object
            table_id: Optional table ID
        
        Returns:
            List of dictionaries representing table rows
        """
        if table_id:
            table = soup.find('table', id=table_id)
        else:
            table = soup.find('table')
        
        if not table:
            return []
        
        # Get headers
        headers = []
        header_row = table.find('thead')
        if header_row:
            headers = [th.get_text(strip=True) for th in header_row.find_all('th')]
        
        # Get rows
        rows = []
        tbody = table.find('tbody')
        if tbody:
            for tr in tbody.find_all('tr'):
                cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
                if headers and len(cells) == len(headers):
                    rows.append(dict(zip(headers, cells)))
                else:
                    rows.append({'data': cells})
        
        return rows


class ArticleScraper(WebScraper):
    """Specialized scraper for articles."""
    
    def scrape_article(self, url: str) -> Dict:
        """
        Scrape article content
        
        Args:
            url: Article URL
        
        Returns:
            Dictionary with article data
        """
        soup = self.fetch_page(url)
        
        # Extract common article elements
        article = {
            'url': url,
            'title': self._extract_title(soup),
            'content': self._extract_content(soup),
            'meta': self._extract_meta(soup)
        }
        
        return article
    
    def _extract_title(self, soup: BeautifulSoup) -> str:
        """Extract article title."""
        # Try multiple selectors
        title = soup.find('h1')
        if not title:
            title = soup.find('title')
        return title.get_text(strip=True) if title else ""
    
    def _extract_content(self, soup: BeautifulSoup) -> str:
        """Extract article content."""
        # Try common article containers
        article = soup.find('article')
        if not article:
            article = soup.find('div', class_='content')
        if not article:
            article = soup.find('main')
        
        if article:
            # Get all paragraphs
            paragraphs = article.find_all('p')
            return '\n\n'.join(p.get_text(strip=True) for p in paragraphs)
        return ""
    
    def _extract_meta(self, soup: BeautifulSoup) -> Dict:
        """Extract metadata."""
        meta = {}
        
        # Extract meta tags
        for tag in soup.find_all('meta'):
            name = tag.get('name') or tag.get('property')
            content = tag.get('content')
            if name and content:
                meta[name] = content
        
        return meta


def main():
    """Example usage of web scraper."""
    # Note: This example uses a public test site
    # Replace with actual URLs for real scraping
    
    print("Web Scraper Example")
    print("Note: Always check robots.txt and terms of service before scraping!")
    print("This is a demonstration of the scraping techniques.")
    
    # Example with quotes.toscrape.com (a site designed for scraping practice)
    scraper = WebScraper('http://quotes.toscrape.com', delay=1.0)
    
    try:
        soup = scraper.fetch_page('http://quotes.toscrape.com')
        
        # Extract quotes
        quotes = scraper.extract_text(soup, '.quote .text')
        print(f"\nFound {len(quotes)} quotes")
        if quotes:
            print(f"First quote: {quotes[0]}")
        
        # Extract authors
        authors = scraper.extract_text(soup, '.quote .author')
        if authors:
            print(f"First author: {authors[0]}")
        
    except Exception as e:
        logger.error(f"Error in scraping example: {e}")
    
    print("\nScraper example completed!")


if __name__ == "__main__":
    main()
