import json
import re

class Indexer:
    def __init__(self):
        self.inverted_index = {}

    def clean_text(self, text):

        text = text.lower()
        words = re.findall(r'\b\w+\b', text)
        return words

    def add_document(self, url, text):
        words = self.clean_text(text)
        for position, word in enumerate(words):
            if word not in self.inverted_index:
                self.inverted_index[word] = {}
            
            if url not in self.inverted_index[word]:
                self.inverted_index[word][url] = []
            
            self.inverted_index[word][url].append(position)

    def save_index(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.inverted_index, f, indent=4)

    def load_index(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.inverted_index = json.load(f)
            return True
        except FileNotFoundError:
            print(f"Error: Index file '{file_path}' not found. Please run the 'build' command first.")
            return False

    def print_word(self, word):
        word = word.lower()
        if word in self.inverted_index:
            print(f"Word '{word}' found in the following pages:")
            print(json.dumps(self.inverted_index[word], indent=4))
        else:
            print(f"Word '{word}' not found in the index.")

    def find_query(self, query):
        words = self.clean_text(query)
        if not words:
            print("Please enter a valid search query.")
            return

        result_urls = None
        for word in words:
            if word in self.inverted_index:
                urls_with_word = set(self.inverted_index[word].keys())
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