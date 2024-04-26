# mapping means we divide and give works to multiple cores
# the process of aggregating the results back is known as reduce
# using pool will speed up your processing time significantly as it divises the tasks


# from multiprocessing import Pool


# def fun(n):
#     return n*n

# if __name__ == "__main__":
#     array = [1,2,3,4,5]
#     p = Pool()
#     p.map(fun,array)
#     result = p.map(fun,array)

#     print(result)

from multiprocessing import Pool
import time

def fun(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

if __name__ == "__main__":
    t1= time.time()
    p = Pool()
    result = p.map(fun,range(100000))
    p.close()
    p.join()

    print(f"Pool took {time.time() - t1}")

    t2 = time.time()
    result=[]
    for x in range(100000):
        result.append(fun(x))
    print(f"serial processing took: {time.time() - t2}")        