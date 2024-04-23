# try:
#     raise MemoryError('memory error') # 'raise' keyword is used to raise an exception in a code
# except MemoryError as me:
#     print(me)

class accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_exception(self):
        print(f"User Defined Exception: {self.msg}")    

try :
    raise accident('Crash between two vehicles') # this is used to raise an exception by the user whenever needed
except accident as a:
    a.print_exception()    


class process_file():
    try:
        f = open("D://100-days-of-python//Python-CodeBasics//book.txt")
        x = 1/0
    except FileNotFoundError as fe:
        print("inside except")    

    finally: # this ensures that it will execute irrespective of the errors which arent handled
        print("Cleaning up th file")   
        f.close()    
