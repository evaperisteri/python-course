my_list = [1, 2, "Hello", [3, 4, 5]]
print("At the start")
for item in my_list:
    print(f"{item} : {id(item)}")

new_list = my_list * 2
print("Duplicated list:", new_list)

new_list[0] = 100
print("Modified list:", new_list)

new_list[3][0] = 300
print("Modified list (2):", new_list)

print("New print")
for item in new_list:
    print(f"{item}: {id(item)}")