from urllib.request import urlopen

import json
import random
from base64 import b64decode, b64encode

url = 'https://raw.githubusercontent.com/luabud/wordle/main/encoded_words.json'

response = urlopen(url)

data_json = json.loads(response.read())
encoded_words = data_json["encoded_words"]

GAME_LENGTH = 5
current_turn = 0
previous_guesses = {i + 1: "" for i in range(GAME_LENGTH)}

answer_word = random.choice(encoded_words)

def game_over(status):
    if status == "win":
        print("Congratulations, you guessed correctly!")
    else:
        decoded_word = b64decode(answer_word).decode('utf-8')
        print(f"Sorry, you lost. The correct word was {decoded_word}")

    current_turn = 0
    return


def wrong_guess_length(guess_word):
    if (len(guess_word) < 5):
        print("Not enough characters.")
    else:
        print("Too many characters.")
    print("Try a guess with 5 letters.")


def is_right_guess(guess, word):
    return str(b64encode(guess.encode("utf-8")), "utf-8") == word


def print_output(guess_word, green_letters, yellow_letters, gray_letters):
    output = []
    for i, g in enumerate(guess_word):
        pair = i, g
        if pair in green_letters:
            output.append(f" {g} ")
        elif pair in yellow_letters:
            output.append(f"({g})")
        else:
            output.append(" _ ")

    previous_guesses[current_turn] = " ".join(output)
    for i in previous_guesses.keys():
        print(f"{i} : {previous_guesses[i]}")

def guess_word(guess_word):

    if len(guess_word) != 5:
        return (wrong_guess_length(guess_word))

    global current_turn
    current_turn += 1

    if current_turn > GAME_LENGTH:
        return game_over("lose")

    answer_pairs = set(enumerate(str(b64decode(answer_word), "utf-8")))
    guess_pairs = set(enumerate(guess_word))

    green_letters = answer_pairs & guess_pairs

    answer_pairs -= green_letters
    guess_pairs -= green_letters

    yellow_letters = set()
    for guess in guess_pairs:
        for answer in answer_pairs:
            if guess[1] == answer[1]:
                answer_pairs.remove(answer)
                yellow_letters.add(guess)
                break

    gray_letters = guess_pairs - yellow_letters

    print_output(guess_word, green_letters, yellow_letters, gray_letters)

    if is_right_guess(guess_word, answer_word):
        return game_over("win")
    if current_turn == GAME_LENGTH:
        return game_over("lose")


while True:

    guess_word(input())
    command = input('If you want to stop choose: Stop or press enter to continue')

    True if command != 'Stop' else False



