import multiprocessing

# passing arguments using value and array
def calc_square(numbers,result,v):
    v.value = 6.0 # here we set a value and that with will be passed as an argument in the funtion and then it will return the same value that we assigned. we assign value in child process and can be accesed by the parent process to set the value
    for index, n in enumerate(numbers):
        result[index] = n*n
    # print(f"Inside result: {result}")




if __name__ == "__main__" :
    numbers = [2,3,4,5]
    result = multiprocessing.Array('i',4) # here i stands for integer
    v = multiprocessing.Value('d',0.0)
    p= multiprocessing.Process(target=calc_square,args=(numbers,result,v))
    p.start()
    p.join()

    print(result[:]) # another method to print all the values of an array
    print(v.value) 

