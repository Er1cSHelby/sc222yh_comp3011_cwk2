import unittest
from src.search import Searcher
from src.indexer import Indexer

class TestSearch(unittest.TestCase):
    def test_phrase_search(self):
        mock_index = {
            "good": {"https://quotes.toscrape.com/page/1/": [0], "https://quotes.toscrape.com/page/2/": [0]},
            "friends": {"https://quotes.toscrape.com/page/2/": [1]}
        }
        searcher = Searcher(mock_index)
        indexer = Indexer()
        
        try:
            searcher.find_query("good friends", indexer.clean_text)
            success = True
        except Exception:
            success = False
            
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()