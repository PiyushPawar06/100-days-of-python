def format_name(f_name,l_name):
    # print(f_name.title()) #title() is used to uniform the string were the first letter is always capital
    # print(l_name.title())

    # this is funtions with outputs were we store the output of the funtion in  an variable and later call that variable whenever requried
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    # print(f"{formated_f_name} {formated_l_name}")
    return f"{formated_f_name} {formated_l_name}" #here when you use the return funtion the called funtion below is replaced by the the return.

formated_string = format_name("piyush","PAWAR")    
print(formated_string) # or you can directly pass the format_name funtion in the print statement

# multiple return statements 
def format_name1(f_name1,l_name1):
    """This is a docstring which is used to write a multiline comment in  the code and should always be written after the defining the funtion.ie:- after the colon of the defined funtion. in docstring we usually type down the basic explaintion of the code in  the function in order make understand the user what exactly the code is written to perform."""
    if f_name1 == "" or l_name1 == "":
        return "You entred invalid input(s)!"
    format_f_name1 = f_name1.title()
    format_l_name1 = l_name1.title()
    return f"Result: {format_f_name1} {format_l_name1}"

print(format_name1(input("What is your first name? "),input("What is your last name? ")))
