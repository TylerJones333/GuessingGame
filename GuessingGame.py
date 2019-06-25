#Createed by Tyler Jones
#Created December 4, 2017
#Udemy class
import random

#GET GUESS
def get_guess():
    return list(input("What is your guess?"))

#GENERATE COMPUTER CODE 123
def generate_code():
    digits = [str(num) for num in range (10)]
    #Shuffle the digits digits
    random.shuffle(digits)
    #Grab the first 3
    return digits[:3]

#GNERATE THE CLUES
def generate_code(code, user_guess):
    if user_guess==code:
        return"CODE CRACKED!!!"
    clues = []

    #Cheacks the given numbers to determine the accuracy of the guess.
    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("Close")

    #Checks if the number is way off.
    if clues == []:
        return("Nope!")
    else:
        return clues
#Welcoming message to the gamer
print("Welcome code breaker!")
secret_code = generate_code()
    clue_report = []

    #Reveals the hidden number.
    while clue_report != "CODE CRACKED!!!":
        guess = get_guess()
        clue_report = generate_clues(guess, secret_code)
        print("here is the result of your guess: ")
        for clue in clue_report:
            print(clue)


#RUN GAME LOGIC
