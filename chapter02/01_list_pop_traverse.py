ages = [19, 23, 34, 55, 19]

print("Initial list of ages:", ages)

for age in ages:
  print(age, end=" ")
  print()

for age in ages:
  print(age, end= ", ")
print()

for index, value in enumerate(ages): #Η enumerate δεν διαβαζει το ιντεξ απλα σαν default ξεκιναει από το 0
  print(f"Index: {index}, Value: {value}")

  