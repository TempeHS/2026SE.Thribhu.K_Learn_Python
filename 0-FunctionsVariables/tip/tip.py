def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    # remove prefix ($)
    result = d.replace('$', '')
    # convert to float
    return float(result)


def percent_to_float(p: str) -> float:
    # remove suffix (%)
    result = p.replace('%', '')
    result = (float(result)/float(100))
    return result


main()