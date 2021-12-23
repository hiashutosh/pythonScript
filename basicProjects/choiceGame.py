#!/usr/bin/env python3
def crossroad():
    choice = input("You are on a crossroad. Which way you want to move (forward/right/left)? ").lower()
    return choice

def river():
    choice = input("You see a river. Do you want to swim or go around (swim/around)? ").lower()
    return choice

def mountain():
    choice = input("You see a mountain with a tunnel. Do you want to climb or go inside tunnel (climb/tunnel)? ").lower()
    return choice

def forest():
    choice = input("You see a forest. Do you want to move forward or camp (forward/camp)? ").lower()
    return choice

def game():
    print("""Welcome to my first game!! 
        NOTE: At any time you want to stop playing. Type: quit
        """)
    name = input("Please enter your name. ")
    age = int(input("please enter your age. "))
    
    if age >= 18:
        print("Hello", name, "you are", age, """years old.
You are alllowed to play""")

        to_play = input("Do you want to play? ").lower()
        if to_play == "yes":
            print("Stating the game..")

            fisrt_c = crossroad()
            if fisrt_c == "quit":
                print("You Quit... See Ya...")
                exit()
            elif fisrt_c == "forward":
                second_c = forest()
            elif fisrt_c == "right":
                second_c = river()
            else:
                second_c = mountain()
            
            if second_c == "quit":
                print("you Quit... See Ya...")
                exit()
            elif second_c == "forward":
                print("you reached home... You are SAFE !!!")
            elif second_c == "camp":
                print("A tiger killed you... You DIE !!!")
            elif second_c == "swim":
                print("you drown... You DIE !!!")
            elif second_c == "around":
                print("you found gold... You are RICH!!!")
            elif second_c == "climb":
                print("You fell... You DIE !!!")
            elif second_c == "tunnel":
                print("you found a Diamond mine... You are RICH !!!")

game()
