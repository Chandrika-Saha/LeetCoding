import random
import time

MAX_HEALTH = 5
def intro():
    print("You are lost in a Haunted Forest...")
    print("Every turn, you must choose one of three paths.")
    print("Some paths hide ghosts, some hide treasure,")
    print("and one might even hide a magic portal to escape!")
    print("-" * 40)

def choose_path():
    choice = ""
    while choice not in ("1", "2", "3"):
        choice = input("Which path will you take? (1 / 2 / 3): ").strip()
    return choice

def resolve_event(path, health, score):
    # TODO: randomly pick an event and update health/score
    # return updated_health, updated_score, has_won
    events = ["ghost", "treasure", "healer", "portal"]
    event = random.choice(events)
    has_won = False

    print("\nYou are following the path...")
    time.sleep(1)

    if event == "ghost":
        print("A terrifying ghost appear! It lets out a chilling scream!!!")
        health -= 1
        print("You ran away in fear, and lost 1 health!")

    elif event == "treasure":
        treasure = random.randint(5, 50)
        print("You find a hidden chest filled with treasures!!!")
        print(f"You gathered {treasure} gold coins!!!")
        score += treasure

    elif event == "healer":
        print("A forest healer appears and heals you wounds...")
        heal = 1
        old_health = health
        health = min(MAX_HEALTH, health + 1)
        gained = health - old_health
        if gained > 0:
            print(f"You are feeling stronger.."
                  f"your health increased by {gained}")
        else:
            print("You already have your maximum health.. "
                  "You cannot be more strong!!!")

    elif event == "portal":
        print("A magical portal opens in front of you!")
        print("You step through it and escape the haunted forest!!!")
        has_won = True

    print(f"\n\t---Current heath: {health}, Current Score: {score}\n---")

    return health, score, has_won

def show_status(health, score, turn):
    print(f"--- Turn {turn} ---")
    print(f"Health: {health}")
    print(f"Score: {score}")
    print("-" * 20)

def play_again():
    ans = input("Do you want to play again? (yes/no): ").lower().strip()
    return ans in ("yes", "y")

# Main game loop
playing = True

while playing:
    health = 3
    score = 0
    turn = 0

    intro()

    game_over = False
    while not game_over:
        turn += 1
        show_status(health, score, turn)

        path = choose_path()
        print(f"You walk along path {path}...")
        time.sleep(1)

        health, score, has_won = resolve_event(path, health, score)

        # TODO: check win/lose conditions here
        # if health <= 0: ...
        # if has_won or score >= 50: ...
        if health <= 0:
            print("You lost!")
        elif has_won or score >= 50:
            print("You won!")

    playing = play_again()

print("Thanks for playing Haunted Forest Escape!")
