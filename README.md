# COMP3011 Coursework 2

## Overview 
The program has three main parts:

**Crawler**: It visits https://quotes.toscrape.com page by page. For each quote, it collects the quote text, the author name, and the tags. It waits 6 seconds between each page request to be polite to the server.

**Indexer**: It takes everything the crawler collected and builds an inverted index. Each word maps to a list of URLS and the positions where that word appears. The index is saved to a JSON file so you do not have to crawl again every time.

**Searcher**: It loads the saved index and searches for your query. If you type more than one word, it finds pages that contain all of them.

## Project Structure
SC222YH_COMP3011_CWK2/
    src/
        crawler.py
        indexer.py
        search.py
        main.py
    tests/
        test_crawler.py
        test_indexer.py
        test_search.py
    data/
        index.json
    requirements.txt
    README.md

## Setup
This project requires Python 3.x and following external libraries:
**`requests`**: Used to handle HTTP GRT requests and retrieve HTML content.
**`beautifulsoup4`**:Used to parse the fetched HTML and extract quotes, authors, and tags.

You can install those packages:

```bash
pip install -r requirements.txt
```

## Run
All commands go through `main.py`

**Build the index from scratch**

```bash
python main.py build
```

**Load and verify the index**

```bash
python main.py load
```

**Look up a specific word in the index**

```bash
python main.py 'anyword you can type here'
```

**Search for a phrase**

```bash
python main.py find 'anyword you can type here'
```

## Running the Tests
```bash
python -m unittest tests/test_crawler.py
python -m unittest tests/test_indexer.py
python -m unittest tests/test_search.py
```
The crawler test checks that the 6-second politeness window is respected. The indexer test checks that word positions are recorded correctly. The search test checks that multi-word queries run without errors.