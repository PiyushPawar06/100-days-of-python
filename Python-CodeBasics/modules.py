import math
import calendar
import funtions_in_python as f #this will help you in reducing the width of code as you use only the letter f instead of the entire name of the module which is funtions_in_python.

# if the module is not in the same directory and is in a sub_directory you have to pass the directory_name.module_name which you wanna import.

# When the module is entirely in a different directory you have to import sys and then pass the path of the module the code would look like below :

# import sys 
# sys.path.append(the path of the module)
# import module_name

# print(math.sqrt(16))
# print(math.pow(2,5))
# print(dir(math))

# cal =calendar.month(2025,4)
# print(cal)

area = f.area_of_square(5)
print(area)
calc = f.basic_math_opreations(10,1)
print(calc)