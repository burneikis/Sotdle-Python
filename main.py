from islandslist import Islands
from PIL import Image
import random
import os

def show_answer_image():
    dirname = os.path.dirname(__file__)
    ImagePath = os.path.join(dirname, answer["Image"])
    answer_image = Image.open(ImagePath)
    answer_image.show()

def is_island(guess):
    for x in Islands:
        if x["Name"] == guess:
            return True

    return False

def get_island(guess):
    for x in Islands:
        if x["Name"] == guess:
            return x

def is_win(guess):
    if answer["Name"] == guess:
        return True

    return False

def is_same_region(guess):
    return answer["Region"] == guess["Region"]

def is_same_x(guess):
    return answer["LocationX"] == guess["LocationX"]

def is_near_x(guess):
    return abs(ord(answer["LocationX"]) - ord(guess["LocationX"])) <= 8

def is_same_y(guess):
    return answer["LocationY"] == guess["LocationY"]

def is_near_y(guess):
    return abs(answer["LocationY"] - guess["LocationY"]) <= 8

def direction(guess):
    if answer["LocationY"] - guess["LocationY"] > 0:
        direction = "N"
        if ord(answer["LocationX"]) - ord(guess["LocationX"]) > 0:
            direction += "W"
        elif ord(answer["LocationX"]) - ord(guess["LocationX"]) < 0:
            direction += "E"
            
    elif answer["LocationY"] - guess["LocationY"] < 0:
        direction = "S"
        if ord(answer["LocationX"]) - ord(guess["LocationX"]) > 0:
            direction += "W"
        elif ord(answer["LocationX"]) - ord(guess["LocationX"]) < 0:
            direction += "E"
    
    return direction

def main():
    global answer
    answer = random.choice(Islands)

    guesses = []
    no_of_guesses = 0

    show_answer_image()

    while no_of_guesses < 6:
        guess = input("Guess the island: ")
        if not is_island(guess):
            print("Not an island")
            continue

        if is_win(guess):
            print("Win ")
            break

        if guess in guesses:
            print("Try something else")
            continue

        guesses.append(guess)

        guess = get_island(guess)

        if is_same_region(guess):
            print(guess["Region"] + " (GREEN)")

        if is_same_x(guess):
            print(guess["LocationX"] + " (GREEN)")
        elif is_near_x(guess):
            print(guess["LocationX"] + " (YELLOW)")

        if is_same_y(guess):
            print(f"{guess['LocationY']} (GREEN)")
        elif is_near_y(guess):
            print(f"{guess['LocationY']} (YELLOW)")

        print(direction(guess))

        no_of_guesses += 1
        print(f"Incorrect. (You have {6 - no_of_guesses} guesses remaining)")

main()