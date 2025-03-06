def main():
    num1 = int(input("First: "))
    operator = input("Operator: ")
    num2 = int(input("Last: "))
    
    ui_output = ""
    
    match operator:
        case '+':
            ui_output = num1 + num2
        case '-':
            ui_output = num1 - num2
        case '*':
            ui_output = num1 * num2
        case '/':
            ui_output = num1 / num2
        case _:
            ui_output = "Not a valid operator"
    
    print(ui_output)

main()