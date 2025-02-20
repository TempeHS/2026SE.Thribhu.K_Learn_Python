cart = dict()

def main():
    
    groceries = []
    
    while True:
        try:
            item = input("Add in your grocery item: ").upper()
        except EOFError:
            print("\n\nHere is your list: ")
            break
        else:
            groceries.append(item)
        
    format_list(groceries)
    

def format_list(list: list):
    list.sort()
    
    other_list = []
    for item in list:
        if item not in other_list:
            other_list.append(item)
    for item in other_list:
        print(f"{list.count(item)} {item}")


if __name__ == '__main__':
    main()