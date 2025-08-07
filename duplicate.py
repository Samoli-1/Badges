my_list = input("Enter : ")

duplicate = []
for item in my_list:
    if my_list.count(item) > 1 and item not in duplicate:
        duplicate.append(item)
print(duplicate)