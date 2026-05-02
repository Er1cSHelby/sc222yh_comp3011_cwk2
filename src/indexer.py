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
