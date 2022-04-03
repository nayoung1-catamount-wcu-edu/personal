import requests
import random
import click

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
words = response.content.decode().splitlines()


def get_word():
    word_choice = random.choice(words)
    return word_choice.upper()


def play(word_choice):
    word_completion = "_" * len(word_choice)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    losses = 0
    wins = 0
    print("Let's play Hangman!")
    print("You have", tries, "attempts to guess the word.")
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word_choice:
                print(guess + " is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job, " + guess + "is in the world!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word_choice) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word_choice) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word" + guess)
            elif guess != word_choice:
                print(guess + " is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word_choice
        else:
            print("Not a valid guess.")
        print("You have", tries, "tries left.")
        print(word_completion)
        print("\n")
    if guessed:
        wins += 1
        print("Congrats, you guessed the word! You win!")
    else:
        losses += 1
        print(
            "Sorry, you ran out of tries.  The word was "
            + word_choice
            + ". Maybe next time!"
        )


def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N) ").upper() == "Y":
        click.clear()
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
