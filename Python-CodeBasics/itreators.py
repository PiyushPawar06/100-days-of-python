# a = ["hey","bro","how","are","you","?"]
# for word in a: # the process of going through the above string one by one and assigning the value is called  itreation
#     print(word)

# itr = iter(a)   
# print(next(itr)) 
# itr = reversed(a) # used to reverse the itreation 
# print(next(itr))

class remotecontrol():
    def __init__(self):
        self.channels = ["HBO","cnn","bbc","espn"]
        self.index = -1

    def __iter__(self):
        return self    
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]

r = remotecontrol()        
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

