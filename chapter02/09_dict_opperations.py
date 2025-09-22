#populate dict
products = {
  1:"apple",
  2:"banana",
  3:"honey",
  4:"mellon"
}

print(f"Initial dictionary: {products}")

#insert/update a new key value pair
products[5]= "orange"
#products[3]= "orange" -->update
print(f"dictionary after insertion: {products}")

#read an element (access)
product_1 = products[1]
print(product_1)

# product_10 = products[10]
# print(product_10) -->key error

product_1 = products.get(1)
print(product_1)

product_10 = products.get(10) #-->επιστρέφει None 
products.get(10, "Out of stock") #-->επιστρέφει το μηνυμα
print(product_10)

del products[1]
print(f"After deleting key 1 {products}")

removed_item = products.pop(3)
print(f"removed item: {removed_item}")
print(f"After removal: {products}")

removed_item = products.pop(10, "Item not found")
print(f"removed item: {removed_item}")
print(f"After removal: {products}")

#delete: remove the 'last' inserted item with popitem()
key, value = products.popitem()
print(f"key:{key}, value:{value}")
print(products)

key_to_check = 2

if key_to_check in products:
  print(f"key: {key_to_check} exists")
else:
  print(f"key: {key_to_check} does not exist")

#iterate
for i in products:   #->epistrefei ta keys
  print(i)

for key in products: 
  print(key, ":", products[key]) 

print("-----------------")
for key in products.keys():   #the same with the above, more readable
  print(key, ":", products[key]) 

print("-----------------")
for value in products.values():   
  print(value) 

print("-----------------")
for key, value in products.items(): 
  print(f"{key}:{value}") 