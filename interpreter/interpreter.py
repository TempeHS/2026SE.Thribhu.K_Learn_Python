print("Calculator     || Insert your equation (simple)")

_input = input()

def calc(input: str) -> float:
    result = input.split()
    
    x = float(result[0])
    y = float(result[2])
    
    match result[1]:
        case '+':
            return x + y
        case '-':
            return x - y
        case '/':
            if result[2] == 0:
                print("Unable to divide by 0")
                return float(0xffff)
            else:
                return x / y
                
        case '*':
            return x * y
        case '%':
            return x % y
            
        case _:
            print("Unable to find the correct operator")
            return float(0xffff)

print(calc(_input))