#import os is for setting the relative file path
import os

#import random is for picking a random island
import random

#from PIL import Image is for showing the map
from PIL import Image

#from islandlist import Islands is for getting the list of islands from the islandslist.py file
from islandslist import Islands

#This function shows the answer island map
def show_answer_image():
    dirname = os.path.dirname(__file__)
    ImagePath = os.path.join(dirname, answer["Image"])
    answer_image = Image.open(ImagePath)
    answer_image.show()

#This funciton checks if a guess is an island within the island list and returns True if it is
def is_island(guess):
    for x in Islands:
        if x["Name"] == guess:
            return True

    return False

#This function checks if the guess is the answer and returns True if it is
def is_win(guess):
    if answer["Name"] == guess:
        return True

    return False

#This function finds the information (region, coords) for the island guessed
def get_island(guess):
    for x in Islands:
        if x["Name"] == guess:
            return x

#This function checks if the guess is in the same region as the answer and returns True if it is
def is_same_region(guess):
    return answer["Region"] == guess["Region"]

#This function checks if the guess is on the same x coordinate as the answer and returns True if it is
def is_same_x(guess):
    return answer["LocationX"] == guess["LocationX"]

#This function checks if the guess is within 8 squares of the x coordinate along the x axis and returns True if it is
def is_near_x(guess):
    return abs(ord(answer["LocationX"]) - ord(guess["LocationX"])) <= 8

#This function checks if the guess is on the same y coordinate as the answer and returns True if it is
def is_same_y(guess):
    return answer["LocationY"] == guess["LocationY"]

#This function checks if the guess is within 8 squares of the y coordinate along the y axis and returns True if it is
def is_near_y(guess):
    return abs(answer["LocationY"] - guess["LocationY"]) <= 8

#This function finds the direction of the answer island from the guess island and returns either "N","NE","E","SE","S","SW","W" or "NW"
def direction(guess):
    if answer["LocationY"] - guess["LocationY"] < 0:
        direction = "N"
        if ord(answer["LocationX"]) - ord(guess["LocationX"]) > 0:
            direction += "E"
        elif ord(answer["LocationX"]) - ord(guess["LocationX"]) < 0:
            direction += "W"

    elif answer["LocationY"] - guess["LocationY"] > 0:
        direction = "S"
        if ord(answer["LocationX"]) - ord(guess["LocationX"]) > 0:
            direction += "E"
        elif ord(answer["LocationX"]) - ord(guess["LocationX"]) < 0:
            direction += "W"
    
    if answer["LocationY"] == guess["LocationY"]:
        if ord(answer["LocationX"]) - ord(guess["LocationX"]) > 0:
            direction = "E"
        elif ord(answer["LocationX"]) - ord(guess["LocationX"]) < 0:
            direction = "W"
    
    return direction

#This is the main function
def main():
    #pick an answer from the island list
    global answer
    answer = random.choice(Islands)

    #create a list of previous guesses
    guesses = []

    #store the number of attempts
    no_of_guesses = 0

    #show answer island map
    show_answer_image()

    #loops until out of guesses (6 times)
    while no_of_guesses < 6:
        #ask for a guess
        guess = input("Guess the island: ")

        #if its not in the island list guess again
        if not is_island(guess):
            print("Not an island")
            continue

        #if they guess correct then they win
        if is_win(guess):
            print("Win ")
            break

        #if they guess something they already tried then guess again
        if guess in guesses:
            print("Try something else")
            continue

        #add the guess to the list of previous guesses
        guesses.append(guess)

        #get the information (region, coords) for the island guessed
        guess = get_island(guess)

        #if the guess is in the same region as the answer then show it as (GREEN)
        if is_same_region(guess):
            print(guess["Region"] + " (GREEN)")

        #if the guess is on the same x coordinate or near it show it as (GREEN) or (YELLOW) accordingly
        if is_same_x(guess):
            print(guess["LocationX"] + " (GREEN)")
        elif is_near_x(guess):
            print(guess["LocationX"] + " (YELLOW)")

        #if the guess is on the same y coordinate or near it show it as (GREEN) or (YELLOW) accordingly
        if is_same_y(guess):
            print(f"{guess['LocationY']} (GREEN)")
        elif is_near_y(guess):
            print(f"{guess['LocationY']} (YELLOW)")

        #print the direction of the answer from the guess
        print(direction(guess))

        #add 1 attempt to the attempt count and check tell the user how many guesses they have left
        no_of_guesses += 1
        print(f"Incorrect. (You have {6 - no_of_guesses} guesses remaining)")

#start the main function
main()