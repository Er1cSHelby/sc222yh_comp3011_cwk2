import unittest
from src.indexer import Indexer

class TestIndexer(unittest.TestCase):
    def test_basic_indexing(self):
        # check that a word is added to the index after indexing a document
        idx = Indexer()
        idx.add_document("url1", "Happy Birthday Happy")
        self.assertIn("happy", idx.inverted_index)
        self.assertEqual(len(idx.inverted_index["happy"]["url1"]), 2)

    def test_case_insensitive(self):
        # 'Good' and 'good' should be treated as the same word
        idx = Indexer()
        idx.add_document("url1", "Good good")
        self.assertEqual(len(idx.inverted_index["good"]["url1"]), 2)

    def test_position_recorded(self):
        # check that word positions are stored correctly
        idx = Indexer()
        idx.add_document("url1", "life is short")
        self.assertEqual(idx.inverted_index["life"]["url1"], [0])
        self.assertEqual(idx.inverted_index["short"]["url1"], [2])

    def test_multiple_urls_same_word(self):
        # the same word in two different pages should appear under both URLs
        idx = Indexer()
        idx.add_document("url1", "life is good")
        idx.add_document("url2", "life goes on")
        self.assertIn("url1", idx.inverted_index["life"])
        self.assertIn("url2", idx.inverted_index["life"])
if __name__ == '__main__':
    unittest.main()