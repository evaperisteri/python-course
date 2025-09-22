#import my_calculations
#from my_calculations import my_add_function
# from my_calculations import my_add_function as my_add
from my_calculations import my_add_function as my_add, num1
num2 = 10
#res = my_calculations.my_add_function(200, 300)
#res = my_add_function(100, 200)
#res = my_add(100, 200)
res = my_add(num1, num2)

print(res)