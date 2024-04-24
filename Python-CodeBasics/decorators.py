# decorators help you to wrap your funtion into a funtion so that you dont clutter different logic of together.


import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} took {str((end-start)*1000)} mil sec.")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    # start = time.time()
    result = []
    for number in numbers:
        result.append(number*number)
    # end = time.time()    
    # print(f"calc_square took {str((end-start)*1000)} mil sec")
    return result    

@time_it
def calc_cube(numbers):
    # start = time.time()
    result = []
    for number in numbers:
        result.append(number*number*number)
    # end = time.time()    
    # print(f"calc_cube took {str((end-start)*1000)} mil sec")   
    return result

array =range(1,10000)
out_square = calc_square(array)
out_cube = calc_cube(array)
