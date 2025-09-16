import math
name = "Alice"
age=20

print("CF7")
print("PI:", math.pi)
print( name, "is", age, "years old")
print("String Concatenation")
# print(name + " is " + age + " years old")
print(name + " is " + str(age) + " years old")
# Python 2 style
print()
print("Python2 style")
print("PI = %6.2f" %math.pi) #6 θέσεις 2 δεκαδικα (αφήνει 3 κενα πριν το 3.14)
print("%s is %d years old" %(name, age))

print("\nPython3 style")
print("Age is {0:2d}".format(age)) #2 ψηφια
print("PI is {0:.3f}".format(math.pi)) #3 δεκαδικα

print("PI = {0:.3f} and age = {1}".format(math.pi, age))

#Alice is 20 years old**
print("{0} is {1} years old".format(name, age), end="**")

#f strings
print(f"{name} is {age} years old.")