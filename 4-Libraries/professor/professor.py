import random
import sys

def main():
    while True:
        level = input("Which level would you like (1, 2, 3): ")
        if not level.isdigit():
            continue
        else:
            match level:
                case '1':
                    questions(1)
                case '2':
                    questions(2)
                case '3':
                    questions(3)
                case _:
                    questions(100)
            break

def questions(level: int):
    completed:int = 0
    chances:int = 0
    
    rand_max:int
    
    if level == 1:
        rand_max = 10
    elif level == 2:
        rand_max = 50
    elif level == 3:
        rand_max = 100
    else:
        rand_max = 99999
    
    while True:
        x = random.randint(0, rand_max)
        y = random.randint(0, rand_max)
        try:
            while chances < 3:
                try:
                    result = int(input(f"{x} + {y} = "))
                    
                    if result != x+y:
                        raise ValueError
                    
                    if result == x+y:
                        completed+=1
                        break
                    
                except ValueError:
                    print("EEE")
                    chances+=1
                    
                    if chances >= 3:
                        print(f"The answer is {x+y}")
                        
        except EOFError:
            print(f"\nSuccessfully completed {completed} questions at Level {level}!")
            return

main()