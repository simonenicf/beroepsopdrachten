import sys
import time

start = True
menu = " "
name = " "
start_sim = " "
retry_input = " "
gameover = 0
bye = 0

# The game menu
def print_menu():
    print (30 * "-" , "Text based adventure" , 30 * "-")
    print ("1. start adventure (intro)")
    print ("2. start adventure (no intro)")
    print ("3. quit")
    print (67 * "-")

# Function to exit the game
def quit():
    print("okay bye")
    exit()

# Start adventure
def adventure():
    input("@: Is anybody there???: ")
    time.sleep(0.5)
    print("@: WHAAAAAA!!!!")
    time.sleep(0.5)
    print("@: Oh sorry. I didn't expect that you where there.")
    time.sleep(0.5)
    print("@: I'm escape simulator.")
    time.sleep(0.5)
    print("@: I'm here to teach you how it is to escape")
    print("@: So shall we start the simulator?")
    print("1. Yes")
    print("2. No")
    print(" ")
    print(67 * "-")
    print(" ")
    run()

def run():
    start_sim = input("Will you start the sim?: ").lower()
    if start_sim == ("1") or start_sim == ("yes") or start_sim == ("y"):
        print("Nyaaa")
        Sim_start()
    elif start_sim == ("2") or start_sim == ("no") or start_sim == ("n"):
        print("@: Uhmmm...")
        print("@: Are you sure?")
        print("1. Yes")
        print("2. No")
        print(67 * "-")
        print(" ")
        run2()
    else:
        print("Put in valid answer.")
        print(" ")
        run()

def Sim_start():
    print("hi")

def run2():
    sure = input("Are you sure?: ").lower()
    if sure == ("1") or sure == ("yes") or sure == ("y"):
        print("@: Ohhh bye then")
        print("You left the simulator alone without going on the adventure.")
        print("You never know what would have happened")
        print(67 * "-")
        print(" ")
        print("GAME OVER")
        print(" ")
        print("ENDING 1")
        print("Nope not going to do this")
        play_again()
    elif sure == ("2") or sure == ("no") or sure == ("n"):
        time.sleep(1)
        print("okay boomer")
        time.sleep(1)
        quit()
    else:
        print("Plz enter valid answer")


def retry():
    print("So do you want to start the simulator?")
    print("1. yes")
    print("2. no")
    retry_input = input("start simulator?: ").lower()
    if retry_input == ("1") or retry_input == ("yes") or retry_input == ("y"):
        print(" ")
    elif retry_input == ("2") or retry_input == ("no") or retry_input == ("n"):
        print("@: ARE")
        time.sleep(1)
        print("@: KIDDING")
        time.sleep(1)
        print("@: ME!!!!!!!")
        print("Good job you made the program so pissed that it blow it self up.")
        print("Now you can't enter the simulator anymore.")
        print(67 * "-")
        print(" ")
        print("GAME OVER")
        print(" ")
        print("ENDING 2")
        print("BYE BYE SIMULATOR")
        play_again()
    else:
        print("Plz enter a valid answer.")
        retry()

def play_again():
    print("Do you want to restart the adventure or go back to menu?")
    print("1. Yes")
    print("2. No")
    print("3. Menu")
    again = input("Restart, quit or menu: ").lower()
    if again == ("1") or again == ("yes") or again == ("y") or again == ("restart"):
        print("Okay")
        print("Good luck on your next run")
        adventure()
    elif again == ("2") or again == ("no") or again == ("n") or again == ("quit"):
        quit()
    elif again == ("3") or again == ("menu") or again == ("m"):
        print("Lets go back")
        print(" ")
        print(67 * "-")
        print(" ")
    else:
        print("Plz enter valid answer")
        play_again()
   
# put the intro here
def intro():
    print("please put intro here")
    adventure()

# starts the game and menu
while start == True:
    print_menu()
    print(" ")
    menu = input("What do you want to do: ")
    print(" ")
    if menu == ("1") or menu == ("intro") or menu == ("start"):
        intro()
    elif menu == ("2") or menu == ("skip"):
        adventure()
    elif menu == ("quit") or menu == ("3"):
        quit()
    else:
        print("Plz enter a valid answer.")
