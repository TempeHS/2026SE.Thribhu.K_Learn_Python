_input = input().lower()


def containsHello(input: str) -> int:
    if _input[0] == 'h':
        if _input.__contains__("hello"):
            return 0
        else:
            return 20
    else:
        return 100


print(containsHello(_input))