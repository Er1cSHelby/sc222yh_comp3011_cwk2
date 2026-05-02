import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

class Crawler:
    def __init__(self):

        self.base_url = "https://quotes.toscrape.com"
        self.visited_urls = set()
        self.crawled_data = [] # Stores the extracted text from each page

    def fetch_page(self, url):
        """
        Sends an HTTP GET request to the specified URL.
        Enforces a strict 6-second politeness window between requests.
        """
        print(f"Fetching URL: {url}")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status() 
            print("Enforcing politeness window: Waiting 6 seconds")
            time.sleep(6)
            
            return response.text
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_page(self, html_content, current_url):
        
        soup = BeautifulSoup(html_content, 'html.parser')
            
        page_text = soup.get_text(separator=' ', strip=True)

        self.crawled_data.append({
            'url': current_url,
            'text': page_text
        })

        next_button = soup.select_one('li.next > a')
        if next_button and next_button.has_attr('href'):
            next_path = next_button['href']
            next_url = urljoin(self.base_url, next_path)
            return next_url
            
        return None 

    def crawl(self):

        print(f"Starting crawl at base URL: {self.base_url}")
        current_url = self.base_url
        
        while current_url and current_url not in self.visited_urls:
            self.visited_urls.add(current_url)
            
            html_content = self.fetch_page(current_url)
            
            if html_content:

                current_url = self.parse_page(html_content, current_url)
            else:
                print("Stopping crawl due to page fetch failure.")
                break
                
        print(f"Crawling complete. Successfully scraped {len(self.crawled_data)} pages.")
        return self.crawled_data

if __name__ == "__main__":
    crawler = Crawler()
    data = crawler.crawl()

    if data:
        print(f"\nSample data from the first page:\nURL: {data[0]['url']}")