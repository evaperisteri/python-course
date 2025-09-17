import random

random_numbers = []
for _ in range(10):
  num = random.randint(1, 100)
  random_numbers.append(num)

print(random_numbers)

#print(f"i = {i}")
#print first even number
for num in random_numbers:
  if num % 2 == 0:
    print(num)
    break

#print last even number
for num in random_numbers:
  if num % 2 == 0:
    even = num #τρεχει όλη τη λίστα και δινει στο even την τιμη του εκαστοτε ζυγου αριθμού
print(even)