
numbers = set(range(1, 11))

even_numbers = {num for num in numbers if num % 2 == 0}

even_list = list(even_numbers)

print("საწყისი სეტი:", numbers)
print("ლუწი რიცხვების სეტი:", even_numbers)
print("ლუწი რიცხვების სია:", even_list)