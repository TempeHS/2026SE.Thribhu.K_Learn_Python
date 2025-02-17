def main():
    print("Input your plate and check whether it is valid")
    plate = input()

    if len(plate) > 6:
        print("Error, it is larger than 6 characters")
        return "Invalid"

    if len(plate) < 2:
        print("Error, it is less than 2 characters")
        return "Invalid"

    if plate[0] == '0':
        print("Error, plate is too short")
        return "Invalid"

    if not plate.isalnum():
        print("Error, plate is not alpha-numeric")
        return "Invalid"
    
    if plate[0] == '0':
        print("Cannot start with 0")
        return "Invalid"

    # AA22AA
    # if the first digit is a number and the last digit is a number, error out

    if not plate[-1].isdigit() and not plate[0].isdigit():
        print("Error, cannot have numbers in the middle of plate")
        return "Invalid"
    
    print("Valid")
    return "Valid"

main()