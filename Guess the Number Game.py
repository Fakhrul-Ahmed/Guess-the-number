print("***Welcome to the guessing game***")

# Importing random module
import random 

# A function is created to start the game
def play_game():
    
    lowest = 1
    highest = 100
    print("I'm thinking of a number between", lowest, "and", highest,".")
    print("Do you want to play?")
    # Selecting the number of chances by the player
    chances = int(input("Choose the number of chances you would like to try: "))
    answer = generate_random_number(lowest, highest) 
    
    guesses = 0
    while True:
        # Taking input from the player
        guess = input("Take a guess (or Q to quit it): ")
        # here Q to show the user quiting the game
        if guess == "Q": 
            print("***Game quitted***")
            break
        guess = int(guess)
        guesses += 1
        if guess == answer:
            print("!!!Congratulations!!! You guessed the number in", guesses, "guesses.")
            break
        elif guess < answer:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        if guesses == chances:
            print("Sorry, you ran out of chances. The number was", answer)
            break

def generate_random_number(low, high):
    return random.randint(low, high)

play_game()
