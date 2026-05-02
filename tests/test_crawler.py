import unittest
import time
from src.crawler import Crawler

class TestCrawler(unittest.TestCase):
    def test_politeness_window(self):
        crawler = Crawler()
        start_time = time.time()
        
        crawler.fetch_page("https://quotes.toscrape.com/page/1/")
        
        duration = time.time() - start_time

        self.assertGreaterEqual(duration, 6, "Politeness window of 6s was not respected")

if __name__ == '__main__':
    unittest.main()