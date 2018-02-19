#!/usr/bin/env python3.6
""" Retrieve and print words form a URL 

Usage: 

    python words.py URL
"""

import sys
from urllib.request import urlopen


def fetch_words(url): 
    """Fech a list of words from a URL.
    
    Args: 
        url: The URL of a UTF-8 document.
        
    Returns: 
        A list of strings containing the words from the
        document    
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_word = line.decode('utf-8').split()
            for word in line_word:
                story_words.append(word)
    return story_words 


def print_items(items):
    """Print a set of items one per line 
    
    Args: 
        An iterable series of printable items
    """
    for word in items: 
        print(word)


def main(url):
    """Print each word from a text document from a URL
    
    Args: 
        url: The URL of a UTF-8 text document
    """
    print(url)
    if url == 'Abort':
        url = "http://humanstxt.org/humans.txt"      
    words = fetch_words(url)
    print_items(words)


if __name__=='__main__':      
    main(sys.argv[1]) # Check argparse / docopt for details on how to parse 
    # [0] is the module filename