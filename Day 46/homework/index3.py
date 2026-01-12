try:
    result = 5 + "10"
    print(result)
except TypeError:
    print("Error: You cannot add an integer to a string")