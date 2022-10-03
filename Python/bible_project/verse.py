import os

from textblob import Sentence
from getbibleverse import verse_lookup
import pandas as pd
from sklearn.model_selection import train_test_split
import nltk
nltk.download('averaged_perceptron_tagger')

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
        pass

    for i in range(len(books)):
        data = pd.json_normalize(verse_lookup(book=books[i], chapter=chapters[i], verses=verses[i]))

        output = pd.concat([output, data], ignore_index=True)

    for index, row in output.iterrows():
        text = nltk.word_tokenize(row['text'])

        print(nltk.pos_tag(text))

except Exception:
    raise Exception