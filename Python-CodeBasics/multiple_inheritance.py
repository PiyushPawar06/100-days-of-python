# multiple inheritance help the child class to access the methods and the properties of two or more different parent classes.

# class father:
#     def gardening(self):
#         print("I love gardening")

# class mother:
#     def cooking(self):
#         print("I love to cook")


# class son(father,mother):
#     def sports(self):
#         print("I love Cricket")        

# s = son()        
# s.sports()
# s.gardening()
# s.cooking()

# another method to inherit the methods and the properties of the parent class/classes into the child class is that you can directly pass the parent_class.property/method() in the properties or methods of child class
class father:
    def skills(self):
        print("gardening,boxing")

class mother:
    def skills(self):
        print("cooking, drawing")


class son(father,mother):
    def skills(self):
        father.skills(self)
        mother.skills(self)
        print("sports,reading")        

s = son()        
s.skills()