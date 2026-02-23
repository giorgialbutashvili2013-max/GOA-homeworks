# append() - ამატებს ელემენტს სიის ბოლოში
numbers = [1, 2, 3]
numbers.append(4)  # [1, 2, 3, 4]

# insert(index, value) - ამატებს ელემენტს კონკრეტულ ინდექსზე
numbers.insert(1, 10)  # [1, 10, 2, 3, 4]

# remove(value) - შლის კონკრეტულ მნიშვნელობას (პირველს რომელიც შეხვდება)
numbers.remove(10)

# pop(index) - შლის ელემენტს ინდექსის მიხედვით და აბრუნებს მას
numbers.pop(0)

# clear() - ასუფთავებს მთელ სიას
numbers.clear()

# index(value) - გვიბრუნებს ელემენტის ინდექსს
nums = [5, 6, 7]
print(nums.index(6))  # 1

# count(value) - ითვლის რამდენჯერ გვხვდება ელემენტი სიაში
nums2 = [1, 2, 2, 3]
print(nums2.count(2))  # 2

# sort() - ალაგებს ზრდადობით
nums2.sort()

# reverse() - აბრუნებს ელემენტების რიგს
nums2.reverse()




text = "hello world"

# upper() - მთელ ტექსტს ხდის დიდ ასოებად
print(text.upper())  # HELLO WORLD

# lower() - მთელ ტექსტს ხდის პატარა ასოებად
print(text.lower())  # hello world

# capitalize() - მხოლოდ პირველ ასოს ხდის დიდად
print(text.capitalize())  # Hello world

# title() - ყველა სიტყვის პირველ ასოს ხდის დიდად
print(text.title())  # Hello World

# strip() - შლის ზედმეტ სიცარიელეს (space) დასაწყისსა და ბოლოში
text2 = "  hi  "
print(text2.strip())  # "hi"

# replace(old, new) - ცვლის ერთ ტექსტს მეორით
print(text.replace("world", "Python"))  # hello Python

# split() - ყოფს ტექსტს სიად
print(text.split())  # ['hello', 'world']

# find() - პოულობს ტექსტის პოზიციას
print(text.find("world"))  # 6



full_name = input("gio albutashvili ")
formatted_name = full_name.title()
print( formatted_name)



numbers = [10, 4, 25, 8, 3]
range_value = max(numbers) - min(numbers)
print( range_value)



