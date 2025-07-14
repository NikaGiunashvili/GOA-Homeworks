elementebi = [25, "hello", True, 3.14, "world", False, "python"]

for item in elementebi:
    if type(item) == str:
        upper_str = item.upper()
        print(upper_str[-3:])