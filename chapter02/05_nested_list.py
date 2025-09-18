items = [1, 2, 3, 14, True, "HelloCF7 friends"]

for item in items:
  print(item, end=" ")
print()

nest_list = [
  [1, 2],
  [3, 4],
  [5, 6]
]

nest_list2 = [[1, 2], [3, 4], [5, 6]]

print(f"first list item: {nest_list[0]}")
print(f"first item on the second nested list: {nest_list[1][0]}")


print(nest_list[1], nest_list[0])
print(nest_list[-2:-3:-1])


