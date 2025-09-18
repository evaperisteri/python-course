bag = { "eggs", "oranges", "bananas"}
print("initial bag:", bag)
# add a new item
bag.add("grapes")
print("Bag after adding grapes:", bag)
#remove
bag.remove("bananas")
print("bag after removing bananas:", bag)
#bag.remove("melon" -->Key Error)

for item in bag: 
  print(item, end=" ")
print()