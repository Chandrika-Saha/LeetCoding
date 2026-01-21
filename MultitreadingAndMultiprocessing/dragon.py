# 🧩 Question (Scenario):
#
# Create a text-based Python game called “Dragon’s Cave.”
#
# In this game, the player stands in front of two caves. In one cave lives a friendly dragon who shares his treasure 🪙.
# In the other cave lives a greedy, hungry dragon who eats anyone who enters! 🐲
#
# The player must choose cave 1 or 2, and the game reveals their fate randomly.
import random
import time

global score
score = 0
def intro():
    print("You are in a land of Dragons!")
    print("There are two caves in front of you....")
    print("In one cave, the dragon has the treasure!!")
    print("In the other cave, the dragon is hungry and will kill you!!!")
    print("Choose wisely.....")

def choose_cave():
    choice = ''
    while choice != '1' and choice != '2':
        choice = input("Which cave you want to enter? 1 or 2?: ")
    return choice

def check_cave(number):
    print(f"You approach the cave {number}...")
    time.sleep(2)
    print("It is very dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out!!!!!")
    time.sleep(1)

    good_dragon = str(random.randint(1, 2))
    return number == good_dragon

def feedback(result):
    global score
    if result:
        score += 5
        print("The dragon smiles.. You won the treasure!!!!")
    else:
        score -= 5
        print("An angry dragon jumped at you!!!")


def riddle_challenge(result):
    global score
    if result:
        print("\nThe friendly dragon smiled: Answer this, and I'll double your treasure...")
        print("Riddle: The more of this there is, the less you see. What is it?")
        answer = input("Your answer: ")
        answer = answer.lower().strip()
        if answer == "dark" or answer == "darkness":
            print("\nThat's Correct!! Here is your double treasure!!!!")
            score *= 2
        else:
            print("\nNooo.. That's wrong... Here is the treasure you got..")
    else:
        print("\nThe angry dragon growls! Answer this, and I might spare you...")
        print("Riddle: I have keys but no locks. I have space but no rooms. "
              "You can enter, but can't go outside. "
              "What am I?")
        answer = input("Your answer: ")
        answer = answer.lower().strip()

        if answer == "keyboard":
            print("\nThat's correct! I spare your life!! Be gone!!")
        else:
            print("\nWrong! (Then it devours you)")

play_again = 'yes'



while play_again.lower() == 'yes' or play_again.lower() == 'y':

    intro()

    choice = choose_cave()
    print(f"You have chosen cave {choice}!!")

    result = check_cave(choice)

    feedback(result)

    riddle_challenge(result)

    print(f"\n-------Your score so far is {score}---------\n")

    play_again = input("\nDo you want to play again? yes/no: ")

print("Bye bye!! Thanks for playing!!")


