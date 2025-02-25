import random

def compare_and_result(player: str, op: str):
    # return true if player won, else return false is not
    
    print(f"Opponent did {op}...")
    
    if player == op:
        return
    
    match player:
        case 'rock':
            if op == 'paper':
                return False
            if op == 'scissors':
                return True
        case 'scissors':
            if op == 'paper':
                return True
            if op == 'scissors':
                return False
        case 'paper':
            if op == 'rock':
                return True
            if op == 'scissors':
                return False

def main():
    playerScore: int = 0
    opponentScore: int = 0
    
    name = input("What is your name? ")
    print(f"Welcome to the rock paper scissors game {name}. Enter CTRL+D to quit\n\n")
    
    try:
        while True:
            player = input(f"Enter your option {name}: [rock, paper, scissors] || ")
            
            options = ['rock', 'paper', 'scissors']
            
            if player not in options:
                print("Make sure it is one of those options")
                break

            op = random.randint(1, 3)
            newvar:str
            match op:
                case 1:
                    newvar = 'rock'
                case 2:
                    newvar = 'paper'
                case 3:
                    newvar = 'scissors'
            
            print(f"DEBUG || Opponent did: {op}")
            
            result = compare_and_result(player, newvar)
            
            
            if result is True:
                print("You won!")
                playerScore+=1
            elif result is False:
                print("You lost :(")
                opponentScore+=1
            else:
                print("Tie, no points!")
                
    except EOFError:
        print(f"\n\nTotal score: \n Player = {playerScore} \n Opponent = {opponentScore}")

main()