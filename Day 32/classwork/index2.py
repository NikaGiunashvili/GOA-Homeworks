# 2) შექმენით ფუნქცია რომელსაც გადაეცემა სია, თუ სია სიგრძე აღემატება 4 ელემენტს დააბრუნეთ რომ  სია ძალიან დიდია, სხვა შემთხვევაში დააბრუნეთ ეს გადმოცემული სია

def check_list(lst):
    if len(lst) > 4:
        return "list is too long"
    else:
        return lst
    
print(check_list([1, 2, 3])) 

print(check_list([1, 2, 3, 4, 5])) 