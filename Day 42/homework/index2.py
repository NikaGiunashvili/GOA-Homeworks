
data = []


def register():
    username = input("Enter your username: ")
    password = input("Enter Your password: ")

    user = {
        "name": username,
        "password": password
    }
    if len(data) == 0:
        print("Registration successfull!")
        data.append(user)
    
    elif len(data) > 0:
        for i in data:
            if i["name"] == user["name"]:
                print("user exsists try another one")
                username = input("Enter another username again: ")
            else:
                print("User registered successfully!")
                data.append(user)
    print(data)
        

register()
register()
register()




def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in data:
        if user["name"] == username and user["password"] == password:
            print("Login successful! Welcome,", username)
        else:
            print("Invalid username or password!")
    
    
    
login()
login()
login()