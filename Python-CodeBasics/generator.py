# # generator is a simple way of creating an itreator
# def remote_control_next():
#     yield "espn" # is use to save memory as it returns only one value and not the enitre thing.
#     yield "cnn"

# itr = remote_control_next()
# print(itr)
# print(next(itr))
# print(next(itr))

# for channel in remote_control_next(): # a Generator can be passed through a loop in order to return the values itreated.
#     print(channel)

# fibonacci series using generator     

def fib():
    a , b = 0 , 1
    while True:
        yield a
        a, b = b , a+b

for f in fib():
    if f > 50:
        break
    print(f)
