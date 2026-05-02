import argparse
from crawler import Crawler
from indexer import Indexer
from search import Searcher

INDEX_FILE = "data/index.json"

def main():
    parser = argparse.ArgumentParser(description="COMP3011 Search Engine Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available core commands")

    subparsers.add_parser("build", help="Crawl the website, build the inverted index, and save it to disk")

    subparsers.add_parser("load", help="Load the pre-built index from the file system")

    print_parser = subparsers.add_parser("print", help="Print the inverted index details for a specific word")
    print_parser.add_argument("word", type=str, help="The word to look up in the index")

    find_parser = subparsers.add_parser("find", help="Find pages containing a specific query phrase")

    find_parser.add_argument("query", type=str, nargs="+", help="The phrase to search for")

    args = parser.parse_args()
    
    indexer = Indexer()

    if args.command == "build":
        print("Starting build process")
        crawler = Crawler()
        crawled_data = crawler.crawl()
        
        print("Building inverted index")
        for page in crawled_data:
            indexer.add_document(page['url'], page['text'])
        
        indexer.save_index(INDEX_FILE)
        print(f"Build complete. Index successfully saved to '{INDEX_FILE}'")

    elif args.command == "load":
        if indexer.load_index(INDEX_FILE):
            print(f"Index successfully loaded from '{INDEX_FILE}'")

    elif args.command == "print":
        if indexer.load_index(INDEX_FILE):
            word = args.word.lower()
            if word in indexer.inverted_index:
                import json
                print(f"Word '{word}' found in:")
                print(json.dumps(indexer.inverted_index[word], indent=4))
            else:
                print(f"Word '{word}' not found.")

    elif args.command == "find":
        if indexer.load_index(INDEX_FILE):
            query_phrase = " ".join(args.query)
            searcher = Searcher(indexer.inverted_index)
            searcher.find_query(query_phrase, indexer.clean_text)

if __name__ == "__main__":
    main()