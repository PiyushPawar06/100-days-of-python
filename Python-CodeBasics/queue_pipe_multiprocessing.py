import multiprocessing


def calc_square(numbers,q):
    for index, n in enumerate(numbers):
        q.put(n*n) # there as the funtinality of queue the elements will be add at the front of the queue and takes out the elements from the front of the queue ie:- fifo




if __name__ == "__main__" :
    numbers = [2,3,4,5]
    q = multiprocessing.Queue()
    p= multiprocessing.Process(target=calc_square,args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get()) # by doing this we get the elements from the front of the queue one by one and print them

# multiprocessing queue and queue module are different then each other.

#   ***multiprocessing queue***          |      ***queue module***
# 1. it lives in shared memeory          | 1. it lives in in-process memory
# 2. used to share data between process  | 2. used to share data between threads