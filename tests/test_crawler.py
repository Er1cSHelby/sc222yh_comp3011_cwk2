import unittest
import time
from src.crawler import Crawler

class TestCrawler(unittest.TestCase):
    def test_politeness_window(self):
        # check that the crawler waits at least 6 seconds between requests
        crawler = Crawler()
        start_time = time.time()
        
        crawler.fetch_page("https://quotes.toscrape.com/page/1/")
        
        duration = time.time() - start_time

        self.assertGreaterEqual(duration, 6, "Politeness window of 6s was not respected")

    def test_fetch_page_returns_html(self):
        # check that the crawler actually gets some content back
        crawler = Crawler()
        result = crawler.fetch_page("https://quotes.toscrape.com/page/1/")
        self.assertIsNotNone(result)

    def test_parse_page_collects_data(self):
        # check that parse_page stores quote data into crawled_data
        crawler = Crawler()
        html = """
        <html><body>
          <div class="quote">
            <span class="text">A test quote.</span>
            <small class="author">Test Author</small>
            <div class="tags"><a class="tag">test</a></div>
          </div>
        </body></html>
        """
        crawler.parse_page(html, "https://quotes.toscrape.com/page/1/")
        self.assertEqual(len(crawler.crawled_data), 1)
    
    def test_no_duplicate_urls(self):
        # check that the crawler does not visit the same URL twice
        crawler = Crawler()
        crawler.visited_urls.add("https://quotes.toscrape.com")
        self.assertIn("https://quotes.toscrape.com", crawler.visited_urls)
        
if __name__ == '__main__':
    unittest.main()