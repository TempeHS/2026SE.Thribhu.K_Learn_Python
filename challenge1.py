# create 2 lists of items
# print the 2 lists as a table
# user input an item to a prompt and only that name from the table prints
# add a new item and sort the lists
# create a text dcument with the lists
# read from the lists
# edit lines and write to lists

import os

def assign(dihlist:list, firstNames:str, lastNames:str, ids:int):
    if len(firstNames) == len(lastNames) == len(ids):
        for i in range(0,len(firstNames)):
            dih = dict(
                id= ids[i],
                fname = firstNames[i],
                lname = lastNames[i]
            )
            dihlist.append(dih)
    print("Done assigning to list")

def print_table(dihlist:list):
    print("ID | First Name | Last Name")
    print("----------------------------")
    if not dihlist:
        print("There are no items in the list...")
        return None
    
    for item in dihlist:
        print(f"{item['id']} | {item['fname']} | {item['lname']}")

# User input an item to a prompt and only that name from the table
def search_keyword(dihlist:list, keyword:str):
    found = False
    input1 = keyword
    for item in dihlist:
        if (str(item['id']) == input1 or input1.lower() in item['fname'].lower() or input1.lower() in item['lname'].lower()):
            print(f"ID: {item['id']}")
            print(f"First Name: {item['fname']}")
            print(f"Last Name: {item['lname']}")
            found = True

    if not found:
        print("Keyword not found :(")

def add_to_list(dihlist:list, Ifname:str, Ilname:str):
    index = 0
    found2 = False
    for item in dihlist:
        if Ifname.lower() in item['fname'].lower() or Ilname.lower() in item['lname'].lower():
            print("Unable to add to list, name already exists")
            found2 = True
        index+=1

    newIndex = index+1
    if not found2:
        dihlist.append(
            dict(
                id=newIndex,
                fname = Ifname,
                lname = Ilname
            )
        )

def read_list_from_file(filename) -> list:
    file = open(filename, 'r')
    list1:list = []
    
    for item in file:
        newItem = item.split('|')
        for i in newItem:
            i.replace(" ", '')
        
        list1.append(dict(
            id=newItem[0],
            fname=newItem[1],
            lname=newItem[2]
        ))
    
    print("Done reading file")
    file.close()
    
    return list1

# Create a text document with the lists
def write_list_to_file(dihlist:list, filename:str):
    file = open(filename, 'w')

    for item in dihlist:
        file.write(f"{item['id']} | {item['fname']} | {item['lname']}\n")
        print(f"Done appending {item['fname']} to file!")

    file.close()

def append_list_to_file(list_input:list, filename:str):
    dihlist = read_list_from_file(filename)
    for item in list_input:
        dihlist.append(item)
    file = open(filename, 'a')

    for item in dihlist:
        file.write(f"{item['id']} | {item['fname']} | {item['lname']}\n")
        print(f"Done appending {item['fname']} to file!")

    file.close()

def fetch_latest_id(filename:str) -> int:
    file = open(filename, 'r')
    lncount = 0
    for i in file:
        lncount+=1
    file.close()
    return lncount

def append_names_to_file(fname,lname, filename:str):
    file = open(filename, 'a')
    id = fetch_latest_id(filename)+1

    file.write(f"{id} | {fname} | {lname}\n")
    print(f"Done appending {fname} to file!")

    file.close()

def main_menu():
    fileCreated:list[bool, str] = [False,""]
    dihlistExists:list[bool, list] = [False, []]
    errString:str = ""
    
    while True:
        print(f"""
------------------------------
        Main Menu:
------------------------------
    {errString}{"\n" if errString else ""}
    1. Create Datafile
    2. Input Data
    3. Read Datafile
    4. Print Data in a table
    5. Search for query
    6. Clean Data
        
------------------------------""")
    
        if fileCreated[0] is True:
            print(f"File exists under name {fileCreated[1]}")
        
        if dihlistExists[0] is True:
            print(f"Data list exists, choose option 4 to print it...")
        
        print("------------------------------")
        
        choice = input("Choice (enter as integer): ")
        try:        
            match choice:
                case "1":
                    # -----------
                    if fileCreated[0]:
                        print("File already exists, create new one?")
                        i = input("Choice (y/n): ")
                        if i == "y":
                            ...
                        elif i == "n":
                            print("Not creating new datafile, returning back to main menu...")
                            errString = "Aborting file creation"
                            continue
                        else:
                            print("Unable to recognise response, returning back to main menu...")
                            errString = "Aborting file creation"
                            continue
                    
                    filename = input("Input a data filename (to be created): ")
                    
                    try:
                        if os.path.isfile(filename):
                            option = input("File exists, overwrite, import or abort? (1,2,3): ")
                            if option == "1":
                                print("Overwriting file")
                                ...
                            elif option == "2":
                                print("Importing file")
                                f = open(filename, 'r')
                                tmpRead = f.readline().split('|')
                                if len(tmpRead) == 3:
                                    print("Successfully validated import, continuing")
                                else:
                                    print("Unable to import file, does not match criteria...")
                                    errString="Unable to import"
                                    continue
                                fileCreated = [True, filename]
                                errString="Imported!"
                                continue
                            else:
                                print("Aborting creation of datafile, returning to menu...")
                                errString = "Aborting datafile creation"
                                continue
                        f = open(filename, 'w')
                        print("No errors creating file")
                        
                        fileCreated[0] = True
                        fileCreated[1] = filename
                        
                        errString = "Success!"
                        continue
                    except IOError as io_e:
                        errString = f"Unable to create file [{io_e}]"
                    except Exception as e:
                        errString = f"Exception occurred [{e}]"
                    # -----------
                    continue
                case "2":
                    # -----------
                    if fileCreated[0] is not True:
                        print("File does not exist, data would not go anywhere. Please choose option 1 before inputting data...")
                        errString = "File does not exist"
                        continue
                    
                    print("Tip: To exit enter Ctrl+Z on windows or Ctrl+D on any others")
                    while True:
                        try:
                            fname = input("Input First Name: ")
                            lname = input("Input Last Name: ")
                            append_names_to_file(fname,lname, fileCreated[1])
                            print("Added...")
                            print("------------------------------")
                        except EOFError:
                            
                            errString = "Success!"
                            break
                    # -----------
                    continue
                case "3":
                    # -----------
                    if fileCreated[0] is not True:
                        print("File does not exist, data would not go anywhere. Please choose option 1 before inputting data...")
                        errString = "File does not exist"
                        continue
                    
                    
                    dihlistExists[1] = read_list_from_file(fileCreated[1])
                    dihlistExists[0] = True
                    
                    print("Successfully read list from file...")
                    errString = "Success!"
                    # -----------
                    continue
                case "4":
                    # -----------
                    if print_table(dihlistExists[1]) == None:
                        errString = "No items in list, try option 3 to read datafile"
                    errString = "Success"
                    # -----------
                    continue
                case "5":
                    # -----------
                    if dihlistExists[0]:
                        search_keyword(dihlistExists[1], input("Enter keyword to search: "))
                        errString = "Success!"
                    else:
                        print("Data list does not exist, please try again")  
                        errString = "File does not exist"
                    # -----------
                    continue
                case "6":
                    # -----------
                    if not fileCreated[0]:
                        print("File does not exist, please choose option 1 to create a new file")
                        errString = "File does not exist"
                        continue
                    choice = input("Do you want to delete the datafile (y/n)?: ")
                    if choice == "y":
                        os.remove(fileCreated[1])
                        fileCreated[0] = False
                        dihlistExists[0] = False
                        errString = "Success!"
                    elif choice == "n":
                        print("Aborting deletion, returning back to main menu")
                        errString = "Aborting data deletion"
                        continue
                    else:
                        print("Unable to determine answer, please try again. Returning back to main menu...")
                        errString = "Aborting data deletion"
                    # -----------
                    continue
                case _:
                    print("Hey, this doesn't exist! Nice try but try again...")
                    continue
        except Exception:
            print("An error occurred while reading choice...")
            errString = "Choose your option properly >:("
            continue

if __name__ == '__main__':
    main_menu()
