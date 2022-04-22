from numpy import indices
import click
import requests
import random
from termcolor import colored


def get_word():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(word_site)
    words = response.content.decode().splitlines()

    word_filter = []

    for word in words:
        if len(word) == 5:
            word_filter.append(word)
        else:
            pass

    word_choice = random.choice(word_filter)

    return word_choice.upper()


def wordle(word_choice):
    word_as_list = list(word_choice)
    guessed = False
    guessed_letters = []
    tries = 6
    score = 0

    click.clear()
    print(word_choice)
    print("Please enter a 5 letter word:")

    while not guessed and tries > 0:
        guess = input("").upper()
        guess_as_list = list(guess)
        if len(guess) == 5 and guess.isalpha():
            if guess == word_choice:
                print(colored(guess, "green"))
                print("You guessed the word with", tries, "attempts left!")
                break
            else:
                for letter in guess:
                    if letter in word_as_list and word_as_list.index(
                        letter
                    ) == guess_as_list.index(letter):
                        correct_correct_pos = colored(letter, "green")
                        guessed_letters.append(correct_correct_pos)
                        score += 1
                    elif letter in word_as_list and word_as_list.index(
                        letter
                    ) != guess_as_list.index(letter):
                        correct_wrong_pos = colored(letter, "yellow")
                        guessed_letters.append(correct_wrong_pos)
                        score += 0.5
                    elif letter not in word_as_list:
                        wrong_wrong_pos = colored(letter, "red")
                        guessed_letters.append(wrong_wrong_pos)
                        score += 0
                    else:
                        pass
                tries -= 1
                word_status = "".join(guessed_letters)
                guessed_letters = []
                print("Guess status: ",word_status)
                print("Score: ",(str(((score / 5) * 100)) + "%"))
                score = 0

        else:
            print("Not a valid guess.")
    else:
        print("Bummer. You did not guess the word today. Better luck next time!")


def get_suggestions():
    return True


def main():
    word = get_word()
    wordle(word)
    while input("Play again? (Y/N) ").upper() == "Y":
        click.clear()
        word = get_word()
        wordle(word)


if __name__ == "__main__":
    main()
