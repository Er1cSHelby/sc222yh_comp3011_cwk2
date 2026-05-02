import json

class Searcher:
    def __init__(self, index_data):
        self.index = index_data

    def find_query(self, query, clean_text_func):

        words = clean_text_func(query)
        
        if not words:
            print("Please enter a valid search query.")
            return

        result_urls = None
        for word in words:
            if word in self.index:
                urls_with_word = set(self.index[word].keys())
                if result_urls is None:
                    result_urls = urls_with_word
                else:
                    result_urls = result_urls.intersection(urls_with_word)
            else:
                result_urls = set()
                break

        if result_urls:
            print(f"Found {len(result_urls)} page(s) containing the query '{query}':")
            for url in result_urls:
                print(f"- {url}")
        else:
            print(f"No pages found containing the phrase: '{query}'")