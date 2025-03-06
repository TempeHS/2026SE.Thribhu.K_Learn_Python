import random
import sys

def main():
    random_number = random.randint(0, int(input("Max Number? ")))
    
    # print(random_number)
    
    while True:
        guess = input("Input guess: ")
        
        if not guess.isdigit():
            print("Not a valid digit")
            continue
        
        guess = int(guess)
        
        if guess > random_number:
            print("Too large!")
        if guess < random_number:
            print("Too small!")
        
        if guess == random_number:
            print("Just right!")
            sys.exit(0)

main()