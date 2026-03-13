
type() ( "ფუნქცია გამოიყენება იმის გასაგებად, თუ რა ტიპის მონაცემია მოცემული ცვლადი.")



num = int("123")
print(type(num))



num = 3.7
a = int(num)
b = float(num)
print(type(a))
print(type(b))



age = "25"
if type(age) == str:
    age = int(age)
print(age)
print(type(age))



num = int("5")
print(num > 3)