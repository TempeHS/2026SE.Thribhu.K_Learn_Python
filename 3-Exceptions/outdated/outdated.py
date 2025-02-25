def main():
    while True:
        date = input("Date: ").title()
        if validate_date(date):
            new_date = convert_date(date)
            if check_for_illegal_dates(new_date):
                break
            else:
                pass
    print(new_date)

def validate_date(date):
    # checks if it has / in it or , (probably not good)
    if "/" in date:
        return True
    elif "," in date:
        return True
    else:
        return False

def convert_date(old_date):
    # old date = mm/dd/yyyy or month day, year
    # this is for mm/dd/yyyy and turns it into yyyy/mm/dd
    if "/" in old_date:
        split_date = old_date.split("/")
        year = split_date[2]
        month = split_date[0]
        day = split_date[1]

        # adds the 0s to the days and months like 1234/07/01
        month = round_to_2(month)
        day = round_to_2(day)
        
        # returns year month day
        return f"{year}-{month}-{day}"
    
    # this is for the month day, year ones
    elif "," in old_date:
        split_date = old_date.replace(",", "").split(" ")
        year = split_date[2]
        month = months[split_date[0]]
        day = split_date[1]

        # convert month string to number
        month = round_to_2(month)
        day = round_to_2(day)

        return f"{year}-{month}-{day}"

# i cooked it with this function becuase it exists in python but its too far gone to do anythihng
def round_to_2(num):
    if len(num) < 2:
        return "0" + num
    else:
        return num

def check_for_illegal_dates(date):
    split_date = date.split("-")
    month = split_date[1]
    day = split_date[2]

    if int(day) <= 31 and int(month) <= 12:
        return True
    else:
        return False





months = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12"
}



main()