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

# product_10 = products.get(10) -->επιστρέφει None 
# products.get(10, "Out of stock") -->επιστρέφει το μηνυμα
# print(product_10)