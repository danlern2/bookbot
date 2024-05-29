#!/usr/bin/env python3
import string
import sys
def main():
    if len(sys.argv) >= 2:
        file = sys.argv[1]
    else:
        file = "bookbot/books/frankenstein.txt"
    bookbot(file)

def bookbot(file):
    try:
    ########  
        file_contents = get_file_contents(file)
        count = wordcount(file_contents)
        sortedlettercount = count_letters(file_contents)

        print(f"--- Begin report of {file} ---")
        print(f"There are {count} words found in the document.\n")
        for letter in sortedlettercount:
            print(f"The '{letter}' character was found {sortedlettercount[letter]} times")
        print("--- End report ---")
    ########
    except FileNotFoundError:
        print(f"The file at {file} was not found.")
    except Exception as e:
        print(f"There was an error:{e}")

def get_file_contents(file):
    with open(file) as f:
        return f.read()

def wordcount(file_contents):
    words = file_contents.split()
    return len(words)  
    # with open(file) as f:
    #     file_text = f.read()
    #     words = file_text.split()
    #     count = len(words)
    #     print(count)

def count_letters(file_contents):
    lettercount = {}
    weight = 0
    mostcommon = []
    alphabet = list(string.ascii_lowercase)
    lowerwords = file_contents.lower()
    for letter in alphabet:
        lettercount[letter] = lowerwords.count(letter)
    sortedletters = dict(sorted(lettercount.items(), key=lambda item: item[1], reverse=True))
    return sortedletters

if __name__ == "__main__":
    main()