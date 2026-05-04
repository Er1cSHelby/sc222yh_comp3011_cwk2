import json
import re

class Indexer:
    """ Build and manage an inverted index from crawled web page content.
        The inverted index maps each word to a dictionary of URL, 
        where each URL maps to a list of positions where the word appears."""
    def __init__(self):
        self.inverted_index = {}

    def clean_text(self, text):

        text = text.lower()
        words = re.findall(r'\b\w+\b', text) # Extract only alphanumeric words
        return words

    def add_document(self, url, text):
        words = self.clean_text(text)
        for position, word in enumerate(words):
            # Add the word to the index if it is not already there
            if word not in self.inverted_index:
                self.inverted_index[word] = {}
             # Add the URL entry for this word if not already there
            if url not in self.inverted_index[word]:
                self.inverted_index[word][url] = []
            
            self.inverted_index[word][url].append(position)

    def save_index(self, file_path):
        """
        Save the inverted index to a JSON file on disk.
        This allows the index to be loaded later without re-crawling.
        """
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.inverted_index, f, indent=4)

    def load_index(self, file_path):
        # Load a previously saved inverted index from a JSON file
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.inverted_index = json.load(f)
            return True
        except FileNotFoundError:
            print(f"Error: Index file '{file_path}' not found. Please run the 'build' command first.")
            return False
