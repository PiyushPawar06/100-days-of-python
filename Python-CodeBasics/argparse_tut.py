# Command line arguments 
# there are two types of arguments positional and optional 
# argparse is an module
# argument is the actual value that is passed in the funtion where as parameters are just a placeholder for that arguments 
import argparse

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help = "first number") # -- is used for optional argument else without -- its positional argument 
    parser.add_argument("--number2", help = "second number") # -h while executing is for help

    parser.add_argument("--operation", help = "operation", choices=["add","sub","multiply"]) # here the choices will help you restrict the operations to just add,sub,multiply anything other then this will give an error

    args = parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None
    if args.operation == "add":
        result = n1+n2
    elif args.operation == "sub":
        result = n1-n2    
    elif args.operation == "multiply":
        result = n1*n2  
    else:
        print("unsupported operation") # if choices are passed above this line of code in unneccesary     
    print(result)

