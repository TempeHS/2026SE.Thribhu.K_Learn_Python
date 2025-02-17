menu = {
		"Baja Taco": 4.25,
		"Burrito": 7.50,
		"Bowl": 8.50,
		"Nachos": 11.00,
		"Quesadilla": 8.50,
		"Super Burrito": 8.50,
		"Super Quesadilla": 9.50,
		"Taco": 3.00,
		"Tortilla Salad": 8.00
	}

confirm = False
total = 0.0

while not confirm:
    menuItem = input("Input your menu item and enter for total: ")
    
    if menuItem == '':
        confirm = True
    
    if menuItem in menu:
        total += menu[menuItem]

print(f"Your total is ${total}")