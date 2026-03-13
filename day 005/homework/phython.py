# and - აბრუნებს True-ს მხოლოდ მაშინ, როცა ორივე პირობა True არის

# or - აბრუნებს True-ს თუ ერთ-ერთი პირობა მაინც True არის

# not - აბრუნებს საპირისპირო მნიშვნელობას (True -> False, False -> True)




print(5 > 3)      # True
print(10 == 10)   # True
print(7 > 4)     # True

print(2 > 5)      # False
print(8 == 3)     # False
print(6 < 2)      # False



print(True and True)     # True
print(True or False)     # True
print(not False)         # True

print(True and False)    # False
print(False or False)    # False
print(not True)          # False



(True and not False) or (False and True) or (not (False or False) and True) and (True or not (False and True))
not False = True
True and True = True
False and True = False
False or False = False
not False = True
True and True = True
False and True = False
not False = True
True or True = True
True or False or True and True
True or False or True
პასუხი: True




(15 + 5 > 10 * 2 and 50 / 5 == 10 or 7 - 2 >= 6) and not (20 < 10 + 15 and 9 / 3 == 2 or 8 - 3 < 2) or (30 / 3 == 10 and (14 - 4 > 5 + 5 or 6 * 2 == 11)) and (40 == 39 + 1 or 12 / 4 != 3)
პასუხი: False
