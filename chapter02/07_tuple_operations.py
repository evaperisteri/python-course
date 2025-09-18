#define a tuple of students

students = ("Alice", "Bob", "Charlie")
print(f"{students}: {type(students)}")
students = "Alice", "Bob", "Charlie" #coma separated values are perceived as tuple
print(f"{students}: {type(students)}")

#iteration
for index, student in enumerate(students):
  print(f"{index}:{student}")

for student in students:
  print(student)

# first_st, second_st, third_st = students[0], students[1], students[2]
first_st, second_st, third_st = students
print(f"first student: {first_st}")
print(f"second student: {second_st}")
print(f"third student: {third_st}")

#students[0] = "Helen" --> TypeError
students = list(students) #convert to list
students[0] = "Helen"
students = tuple(students)

print(f"{students}: {type(students)}")