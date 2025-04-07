# best to use 2 lists instead of a dictionary to make things less complicated :)
list1 = []
list2 = []

# first import the csv as read as "file" variable
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

# iterates through the index of one of the lists
for item in range(len(list1)):
    # prints it out nicely
    print(f"{list1[item]} | {list2[item]}")

# output:
# diddy | babyoil
# potato | hashira
# god | save
# queeny | me
# hello | world

# -tk