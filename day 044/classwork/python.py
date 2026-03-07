try:
    a = float(input("შეიყვანე პირველი რიცხვი: "))
    b = float(input("შეიყვანე მეორე რიცხვი: "))
    result = a / b
    print("პასუხი:", result)
except ZeroDivisionError:
    print("0-ზე გაყოფა არ შეიძლება")







try:
    num = int(input("შეიყვანე რიცხვი: "))
    print("შენი რიცხვია:", num)
except ValueError:
    print("გთხოვ შეიყვანე მხოლოდ რიცხვი")






numbers = [10, 20, 30, 40]

try:
    index = int(input("შეიყვანე ინდექსი: "))
    print("ელემენტი:", numbers[index])

except IndexError:
    print("ასეთი ინდექსი სიაში არ არსებობს")





try:
    num = int(input("შეიყვანე რიცხვი: "))
    print("spuare is:", num ** 2)

except ValueError:
    print("შეიყვანე მხოლოდ რიცხვი")



