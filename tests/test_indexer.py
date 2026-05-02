import unittest
from src.indexer import Indexer

class TestIndexer(unittest.TestCase):
    def test_basic_indexing(self):
        idx = Indexer()
        idx.add_document("url1", "Happy Birthday Happy")
        self.assertIn("happy", idx.inverted_index)
        self.assertEqual(len(idx.inverted_index["happy"]["url1"]), 2)

if __name__ == '__main__':
    unittest.main()