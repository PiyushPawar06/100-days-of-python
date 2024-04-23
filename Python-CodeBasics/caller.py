import entry_point 

print("I am in caller.py")
print(entry_point.calc_area(5,10))
# print(f"{__name__}")
# here the __name__ value changes to entry_point as it becomes the entry point for caller.py but the value of __name__ remains as __main__ in entry_point.py