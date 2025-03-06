array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
number = array[0]
for num in array:
  if num > number:
    number = num
print("number is:", number)