import os

from getbibleverse import verse_lookup
import pandas as pd
from sklearn.model_selection import train_test_split
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')

os.system("cls")

try:
    # Variables as empty lists
    books = []
    chapters = []
    verses = []
    output = pd.DataFrame(columns=["bookname", "chapter", "verse", "text"])
    
    # User input prompts
    num = int(input("Hello! How many Bible verses do you want analyze?\n"))
    if num > 1:
        os.system("cls")
        print("Okay. Let's look at {} verses.".format(num))
        print(
            "Note: When there are multiple books with the same name, they are denoted by '1' rather than '1st' and please use 'Psalms' rather than 'Psalm'. "
        )

        # Store input for the number of verses requested
        for i in range(num):
            while i < num:
                book = input("\nBook name: ").capitalize()
                chapter = input("Chapter number: ")
                verse = input("Verse(s): ")

                books.append(book)
                chapters.append(chapter)
                verses.append(verse)

                if i + 1 < num:
                    os.system("cls")
                    print(
                        "Okay. I've stored "
                        + books[i]
                        + " "
                        + chapters[i]
                        + ":"
                        + verses[i]
                        + ". What's next?"
                    )
                elif i + 1 == num:
                    os.system("cls")
                    print("Okay. I've stored that data.\n")

                i = i + 1
            else:
                break

        os.system("cls")

# Sentiment analysis
    else:
        print('hi')
        pass

    for i in range(len(books)):
        data = pd.json_normalize(verse_lookup(book=books[i], chapter=chapters[i], verses=verses[i]))

        output = pd.concat([output, data], ignore_index=True)
    
    text = " ".join(output.text)

    word_frequencies = {}
    sentence_scores = {}
    punctuation = punctuation + '\n'
    doc = nlp(text)
    
    tokens = [token.text for token in doc]

    for word in doc:
        word = word.text.lower()
        if word not in stopwords:
            if word not in punctuation:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
    
    max_freq = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_freq
    
    sentence_tokens = [sent for sent in doc.sents]
    
    for sent in sentence_tokens:
        for word in sent:
            word = word.text.lower()
            if word in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

    select_length = int(len(sentence_tokens)*0.3)
    summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    print(summary)

except Exception:
    raise Exception