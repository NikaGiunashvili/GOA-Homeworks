name = input("Enter Your Name: ")

has_upper = False 

for i in name:
    if i.isupper():
        has_upper = True
        break

if has_upper:
    print(name.lower())
else:
    print(name.capitalize())
