import unittest
from src.search import Searcher
from src.indexer import Indexer

class TestSearch(unittest.TestCase):
    def setUp(self):
        # a small mock index used in all tests
        self.mock_index = {
            "good": {
                "https://quotes.toscrape.com/page/1/": [0],
                "https://quotes.toscrape.com/page/2/": [0]
            },
            "friends": {
                "https://quotes.toscrape.com/page/2/": [1]
            }
        }
        self.searcher = Searcher(self.mock_index)
        self.indexer = Indexer()
 
    def test_single_word_search(self):
        # searching for a word that exists should not raise any errors
        try:
            self.searcher.find_query("good", self.indexer.clean_text)
            success = True
        except Exception:
            success = False
        self.assertTrue(success)
 
    def test_phrase_search(self):
        # searching for a multi-word phrase should not raise any errors
        try:
            self.searcher.find_query("good friends", self.indexer.clean_text)
            success = True
        except Exception:
            success = False
        self.assertTrue(success)
 
    def test_word_not_in_index(self):
        # searching for a word that does not exist should not crash
        try:
            self.searcher.find_query("nonexistentword", self.indexer.clean_text)
            success = True
        except Exception:
            success = False
        self.assertTrue(success)
 
    def test_empty_query(self):
        # an empty search query should not crash
        try:
            self.searcher.find_query("", self.indexer.clean_text)
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()