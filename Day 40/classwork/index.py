# 1)შექმენით სია სადაც გექნებათ რიცხვები მოცემული და ახალ სიაში ჩაამატეთ ისეთი რიცხვები რომლებიც იყოფა 3ზეც და 5 ზეც

numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

iyopa_samze = [i for i in numbers if i % 3 == 0]

iyofa_xutze = [i for i in numbers if i % 5 == 0] 

print(iyopa_samze)
print(iyofa_xutze)