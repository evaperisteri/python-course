a = range(10)
print(f"Type of a: {type(a)}")

for i in range(10):
  if i == 5:
    break
  print(i, end=" ")
print()

print(i)

for i in range(10):
  if i ==5:
    continue
  print(i, end=" ")
print()
print("-"*10)

for i in range(10):
  if i == 5:
    break  #αν εδω ειχαμε continue θα τελειωνε ο βρογχος αλλα δεν θα εβγαινε οπότε θα εκτελούσε & το else
  print(i, end=" ")
else:
  print("Loop ended normaly")

#List of fruits
fruits = ["Banana", "Orange", "Mango", "Grapes"]

fruit_to_check = "Banana"
for fruit in fruits:
  if fruit == fruit_to_check:
    print(f"{fruit_to_check} is in list")
    break
else:
  print(f"{fruit_to_check} not in list")

#Happy Hour
print("Why do Python devs never get lost?")
print("Because they always know where 'in' is!")

if fruit_to_check in fruits:
  print(f"{fruit_to_check} is in list")
else:
  print(f"{fruit_to_check} not in list")

#Challenge --One line example
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else'not in'} the list")