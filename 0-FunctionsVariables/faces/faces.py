print("Emoticon to emoji converter")
print("Currently supports `:)` and `:(`")
print("Input: ")

_input = input()

output = _input.replace(':)', '🙂').replace(':(', '🙁')
print(output)