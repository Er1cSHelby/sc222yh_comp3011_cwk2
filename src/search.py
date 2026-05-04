import json

class Searcher:
    """ Handles search queries against a pre-built inverted index.
    Supports single-word and multi-word queries."""
    def __init__(self, index_data):
        # The inverted index passed in from the Indexer
        self.index = index_data

    def find_query(self, query, clean_text_func):

        words = clean_text_func(query)

        # Handle empty or invalid input
        if not words:
            print("Please enter a valid search query.")
            return

        result_urls = None
        for word in words:
            if word in self.index:
                # Get all URLs that contain this word
                urls_with_word = set(self.index[word].keys())
                if result_urls is None:
                    # First word initialise the result set
                    result_urls = urls_with_word
                else:
                    # Subsequent words keep only URLs that contain all words so far
                    result_urls = result_urls.intersection(urls_with_word)
            else:
                 # Word not in index at all no pages can match the full query
                result_urls = set()
                break

        if result_urls:
            print(f"Found {len(result_urls)} page(s) containing the query '{query}':")
            for url in result_urls:
                print(f"- {url}")
        else:
            print(f"No pages found containing the phrase: '{query}'")