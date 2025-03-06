import inflect

def main():
    list_of_people = []
    p = inflect.engine()
    try:
        while True:
            list_of_people.append(input("Input your people: "))
            # ['Leslie', 'John']
    except EOFError:
        print(f"Adieu, adieu, to {parse(list_of_people, p)}")

def parse(people_list: list, p) -> str:
    return p.join(people_list)

if __name__ == '__main__':
    main()