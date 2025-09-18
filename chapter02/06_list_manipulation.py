fruits = ["Apple", "Banana", "Cherry", "Apple"]

print(f"Initial list: {fruits}")

#add a fruit at the end of the list
fruits.append("Berry")
print("After adding Berry:", fruits)

#fruits.append("Grapes", "Fig") does not work
#fruits.append(["Grapes", "Fig"]) adds a nested list at the end
fruits.extend(["Grapes", "Fig"])
print("after adding grapes, figs:", fruits)

#insert an element in a specific position
fruits.insert(1, "Coconut")
print("after adding coconut:", fruits)

#update the first element
fruits[0]= "Melon"
print("after updating the first element", fruits)

#update a slice of list(two elements)
fruits[1:3] = ["A", "B", "C"]
print("after updating a slice", fruits)

#pop()
removed_item = fruits.pop(2) # pop() default removes the last if pop(0) removes first
print(f"Removed Item: {removed_item}")
print("After pop():", fruits)

# remove()
fruits.remove("C")
print("After remove('C):", fruits)

# fruits.remove("D") -->value error
# print("After remove('D):", fruits)

idx = fruits.index("A") #idx = fruits.index("B") value error
print(idx)

item_to_remove = "Grapes"
if item_to_remove in fruits:
  fruits.remove(item_to_remove)
  print(f"{item_to_remove} removed")
else:
  print("insert a valid")