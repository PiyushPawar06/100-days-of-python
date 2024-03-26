import os
def clear():
    os.system('cls')

def addition(n1,n2):
    return n1 + n2    

def substrraction(n1,n2):
    return n1 - n2

def multiplication(n1,n2):
    return n1 * n2

def division(n1,n2):
    return n1 / n2

opreations = {"+":addition,
              "-":substrraction,
              "*":multiplication,
              "/":division
             }
def calculator():
    num1 = float(input("Please enter first number: "))
    for symbol in opreations:
        print(symbol)
    should_continue = True
    while should_continue:
        opreation_symbol = input("Please pick the opreation:")
        num2 = float(input("Please enter second number: "))
        calculation_funtion = opreations[opreation_symbol]
        answer = calculation_funtion(num1,num2)

        print(f"{num1} {opreation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
            num1  = answer
        else :
            should_continue = False
            calculator() #recurrsion is used here were we recall the calculator()
            
 
calculator()
