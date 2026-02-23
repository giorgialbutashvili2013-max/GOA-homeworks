ფუნქცია არის კოდის ბლოკი, რომელიც ასრულებს კონკრეტულ დავალებას და შეგვიძლია რამდენჯერაც გვინდა იმდენჯერ გამოვიყენოთ.
ის გვეხმარება კოდის გამარტივებაში, ორგანიზებაში და თავიდან გვარიდებს ერთი და იგივე კოდის გამეორებას.


def function_name():


def greet(name):
    print("გამარჯობა", name)

greet("გიორგი")



def check_numbers(num1, num2):
    if num1 % num2 == 0:
        return num1 * num2
    else:
        return num1 + num2


print(check_numbers(10, 5))  
print(check_numbers(10, 3))



def rectangle(width, height):
    if width == height:
        return width * height
    else:
        return 2 * (width + height)
print(rectangle(5, 5))  
print(rectangle(4, 6)) 




