name = input("Please insert your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height: "))
is_student = input("Are you a student? (Yes/No): ").lower() == "yes" #(Yes, YES, yES)
print(f"Hello {name}!")
if is_student:
  print("You are student")
  print("....")
else:
  print("You are not a student")

print("Your age is {} and your height is {:.2f} meters".format(age, height))