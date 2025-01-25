import random
import sys
from enum import Enum
def Game():
    game_count = 0
    player_win = 0
    python_win = 0
    def rps():
        nonlocal player_win
        nonlocal game_count
        nonlocal python_win
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS =3

        more =True
        while more:
            playerone=input("This game is rock paper scissors.\nChoose the number between 1 to 3.\n1 for rock.\n2 for paper.\n3 for scissors.\n")

            name = int(playerone)

            computer = random.choice("123")
            python =int(computer)

            if name <1 and name>3:
                print("you must enter number between 1 to 3.")
                return rps()
            def gamenum(name,python):
               
                nonlocal player_win
                nonlocal python_win
                if  name == 1 and python == 3:
                    player_win += 1
                    return"you win!😍😍"
                elif name == 2 and python == 1:
                    player_win += 1
                    return"you win!😍😍"
                elif name == 3 and python == 2:
                    player_win += 1
                    return"you win!😍😍"
                elif name == python:
                    
                    return"Tie game!😒😒"
                else:
                    python_win += 1
                    return"You lose the game.❌❌"
            count = gamenum(name,python)       
            print(count)
            print(f"You choose {str(RPS(name)).replace("RPS.","")}")
            print(f"Python choose {str(RPS(python)).replace("RPS.","")}")

           
            game_count += 1
            print(f"Totalgame = {game_count}" )
            print(f"Playerwin = {player_win}" )
            print(f"Pythonwin = {python_win}" )
            
            while True:
                more = input("Do you want to play again?\nY for yes\nE for exit.\n\n")
                if more.lower() not in ["y","e"]:
                    continue
                else:
                    break
            if more.lower() == "y":
                return rps()
            else:
                sys.exit("thankyou for the game.\nif you want to spend time with us you can join us anytime.😊😊")

    rps()
Game()