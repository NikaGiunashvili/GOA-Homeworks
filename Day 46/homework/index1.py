try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Error: That is not a valid number!")