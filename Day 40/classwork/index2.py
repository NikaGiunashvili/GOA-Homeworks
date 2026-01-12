# 2)შექმენით სია სადაც გექნებათ მოცემული სახელები, შემდეგ ახალ სიაში ჩაამატეთ ისეთი სახელები სახელები რომლის სიმბოლოების რაოდენობაც არის ლუწი რიცხვი

names = ["iika", "giorgi", "ana", "luka", "mari"]

luwi_saxelebi = [i for i in names if len(i) % 2 == 0]

print(luwi_saxelebi)