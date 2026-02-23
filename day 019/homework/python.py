# append() - ამატებს ელემენტს სიის ბოლოში

# insert() - ამატებს ელემენტს მითითებულ ინდექსზე

# remove() - შლის კონკრეტულ მნიშვნელობას (პირველს რომელიც შეხვდება)

# pop() - შლის ელემენტს ინდექსის მიხედვით და აბრუნებს მას

# clear() - ასუფთავებს მთელ სიას

# index() - გვიბრუნებს კონკრეტული მნიშვნელობის ინდექსს

# count() - ითვლის რამდენჯერ გვხვდება ელემენტი სიაში

# sort() - ალაგებს სიას ზრდადობით

# reverse() - აბრუნებს სიის ელემენტების რიგს




list = [10, 20, 30, 40]
first_element = list[0]
list.append(first_element)
list.pop(0)
print(list)



list.clear()
list.append("A")
list.append("C")
list.insert(1, "B")
print(list)  



numbers = [1, 2, 3, 4, 5, 6, 7]


if len(numbers) > 5 and numbers[5] == 10:
    
    numbers.pop()
else:
    
    numbers.insert(5, 10)

print(numbers)




numbers = [1, 2, 3, 4, 5, 6, 7]

if len(numbers) > 5 and numbers[5] == 10:
   
    numbers.pop()
else:
    
    numbers.insert(5, 10)

print(numbers)












