# გააკეთეთ იგივე რაც წეღან გავაკეთეთ გაკვეთილზე ომხმარებლის რეგისტრაცია, სადაც მომხმარებელს შეაყვანინებთ მის username ს და პაროლს, ეს ყველაფერი უნფა იყოს dictionary ს სახით და ჩაამატეთ სიაში ეს მონაცემი და გამოიტანეთ ტერმინალში


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