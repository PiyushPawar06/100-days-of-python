import time
import threading
def calc_square(numbers):
    print("claculate square of numbers")
    for n in numbers:
        time.sleep(0.2) # when the pc is busy doing so work like installing a package for example by using multithreading  we can utilize that time for some other task. while waiting here the calc_cube() got excuted and vice-versa
        print(f"square: {n*n}")

def calc_cube(numbers):
    print("claculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print(f"cube: {n*n*n}")

arr= [2,3,4,5]
t = time.time()
t1 = threading.Thread(target=calc_square,args=(arr,)) #line 17 and 18 will execute simlutaneously.
t2 = threading.Thread(target=calc_cube,args=(arr,)) #

t1.start() # to start the execution of funtion
t2.start()

t1.join() # join() delays a program's flow of execution until the target thread has been completely read
t2.join()
print(f"done in time: {time.time() - t}")
