x =input("Please enter the first number: ")
y =input("Please enter the second number: ")
# try:
#     z = int(x) / int(y)
# except Exception as e: # we are pass an exception handling so that there is no termination of the code and the rest of the code executes.
#     print(f"Exception ooccured: {e}")   
#     z = None 
# print(f"The division is: {z}")
try:
    # z = int(x) / int(y)
    z = x / int (y)
except ZeroDivisionError as e: # here we have directly mentioned the error that will occur.
    print(f"Division by zero exception")   
    z = None 
except Exception as ne:
    print(f"Exception type: {type(ne).__name__}")   # this is to retreive the name of the error thrown.
    z = None
print(f"The division is: {z}")