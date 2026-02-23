list-mutable ანუ შეცვლა შეიძლება
tuples-immiutable ანუ შეცვლა არ შეიძლება


info = ("Giorgi", "learning", "programs")
print(info)


def manual_count(lst, element):
    count = 0
    for item in lst:
        if item == element:
        count += 1
    return count



def manual_find(lst, element):
    index = 0
    for item in lst:
        if item == element:
        return index
        index += 1
    return -1




names = ("gio", "ilia", "tato", "gurami", "vaja")

student1, student2, *otherstudents = names   

print(student1)
print(student2)
print(otherstudents)
