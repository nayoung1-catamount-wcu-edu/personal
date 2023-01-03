import os
import pandas as pd
from getbibleverse import verse_lookup

from sklearn.model_selection import train_test_split
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')
punctuation = punctuation + '\n'
word_frequencies = {}
sentence_scores = {}

verses_df = pd.DataFrame(columns=["bookname", "chapter", "verse", "text"])

os.system("cls")

bible_book = input("Book: ").capitalize()
bible_chapter = input("Chapter: ")
bible_verse = input("Verse(s): ")

print("\n")

try:
    if verse_lookup(bible_book, bible_chapter, bible_verse) is None:
        print("That didn't work.")
    else:
        verses = pd.json_normalize(
            verse_lookup(bible_book, bible_chapter, bible_verse)
        )
        verses_df = pd.concat([verses_df, verses], ignore_index=True)
        words = nlp(" ".join(verses_df.text))

    for word in words:
        word = word.text.lower()
        if word not in stopwords:
            if word not in punctuation:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1

    print(word_frequencies)
except ValueError:
    exit