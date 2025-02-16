def fuel(fuel_intake: str):
    try:
        fuel_intake = fuel_intake.split('/')
        
        numerator = int(fuel_intake[0])
        denominator = int(fuel_intake[1])
        
        if denominator != 4:
            raise ValueError()
        if numerator not in [0, 1, 2, 3, 4]:
            raise ValueError()
            
        divide = numerator / denominator
        
        match divide:
            case 1:
                return 'F'
            case 0.75:
                return '75%'
            case 0.50:
                return '50%'
            case 0.25:
                return '25%'
            case 0:
                return 'E'
            case _:
                raise ValueError()
        
    except (ValueError, ZeroDivisionError) as e:
        return str(e)

print(fuel(input("Input fuel: ")))