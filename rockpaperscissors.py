# ask for input of rock paper scissors

import random

def compare_and_result(player: str, op: str) -> bool:
    # return true if player won, else return false is not
    
    print(f"Opponent did {op}...")
    
    if player == op:
        print("Tie!")
        return False
    
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
    while True:
        player = input("Enter your option: [rock, paper, scissors] || ")
        
        options = ['rock', 'paper', 'scissors']
        
        if player not in options:
            print("Make sure it is one of those options")

        op = random.randint(1, 3)
        newvar:str
        match op:
            case 1:
                newvar = 'rock'
            case 2:
                newvar = 'paper'
            case 3:
                newvar = 'scissors'
        
        result = compare_and_result(player, newvar)
        
        if result == True:
            print("You won!")
        else:
            print("You lost :(")

main()