# სია სადაც შევინახავთ დარეგისტრირებულ მომხმარებლებს
data = []


# ფუნქცია რეგისტრაციისთვის
def register():
    # სახელის შეყვანა
    username = input("Enter your username: ")
    
    # პაროლის შეყვანა
    password = input("Create a new password: ")

    # მომხმარებლის მონაცემებს ვინახავთ ლექსიკონში
    current_user = {
        "name": username,
        "password": password
    }

    # თუ data სია ცარიელია
    if len(data) == 0:
        print("Registration successfull!")
        # მომხმარებელს ვამატებთ სიაში
        data.append(current_user)

    # თუ data სიაში უკვე არის მომხმარებლები
    elif len(data) > 0:
        # ვამოწმებთ ყველა არსებულ მომხმარებელს
        for i in data:
            # თუ უკვე არსებობს იგივე username
            if i["name"] == current_user["name"]:
                print("username already exists!")
                
                # ვთხოვთ მომხმარებელს ახალი სახელის შეყვანას
                username = input("Enter another username again: ")
                
                # ვცვლით current_userის სახელს
                current_user["name"] = username
                
                # ვამატებთ სიაში
                data.append(current_user)
                break

            else:
                print("Registration successfull!")
                data.append(current_user)
                break


register()
register()
register()

#ვბეჭდავთ ყველა დარეგისტრირებულ მომხმარებელს
print(data)
