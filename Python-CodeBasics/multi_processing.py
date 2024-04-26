
import multiprocessing
# multi processing uses shared memory here 
def calc_square(numbers):
    for i in numbers:
        print(f"square: {i*i}")

def calc_cube(numbers):
    for i in numbers:
        print(f"cube: {i*i*i}")

if __name__ == "__main__" :
    arr = [2,3,4,5]
    p1 = multiprocessing.Process(target=calc_square,args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")