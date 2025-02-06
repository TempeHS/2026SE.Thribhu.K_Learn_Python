print("What is the meaning of life?")

_input = input();

result = _input.lower();

def IsInputMeaningOfLife(input: str) -> bool:
    if input == '42' or input == 'forty two' or input == 'forty-two':
        return True
    else:
        return False

if IsInputMeaningOfLife(result):
    print("Yes")
else:
    print("No")