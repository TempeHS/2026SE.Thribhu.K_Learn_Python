#crete 2 lists of items
list1 = []
list2 = []

#print the lists as a table
with open("fix/textfile.csv", "r")as file:
    # this reads each line and appends the content in "line" variable
    for line in file:
        # this splits and cleans up the rubbish: 
        # OLD: 'diddy': ' babyoil\n'
        # NEW: diddy, babyoil
        split = line.replace("\n", "").replace(" ", "").split(',')
        # makes it easier for viewing, not required
        key = split[0]
        value = split[1]
        # append to each list
        list1.append(key)
        list2.append(value)

# with open("fix/names.csv") as file:
#     row = lines

print(f"| col 1 | col 2 |" )
print("| ----- | ----- |")
for index in range(len(list1)):
    print(f"| {list1[index]} | {list2[index]} |")

#user inpurt a item to a prompt and only the name from the table prints
def corrospond():
    try:
        input1 = input("Product: ")        
        if input1 in list1 or input1 in list2:
            if input1 in list1:
                print(f"{input1} corresponds with {list1[list1.index(input1)]}")
            else:
                print(f"{input1} corresponds with {list1[list1.index(input1)]}")
        else:
            print("not in list")
    except ValueError:
        print("not in list")
    # Else statement does not have any use -tk
    # else:
    #     False


corrospond()
#add a new item and sort the list
yupornah = input("Add an item; Y/N: ").lower()
inputlist1:str
inputlist2:str
if yupornah == 'y':
    inputlist1 = input("Item Name: ")
    if inputlist1 in list1:
        False
    elif inputlist1 in list2:
        False
    else:
        list1.append(inputlist1)
    inputlist2 = input("Corrosponding Name: ")
    list2.append(inputlist2)


#create a text document with the lists

with open("fix/textfile.csv", "a") as file:
    for index in range(len(list1)):
        file.write(f"{list1[index]}, {list2[index]}")
        file.write("\n")
#read from the lists
with open("fix/textfile.csv") as file:
    for i in range(len(list1)):
        print(f"| {list1[i]} | {list2[i]} |")
#edit lines and write to lists