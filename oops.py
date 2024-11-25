# Inheritance

class SuperNode:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f"Hello, {self.name} -> Parent"
        
class SubNode(SuperNode):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        
    def greet(self):
        print(super().greet())
        return f"Hello, {self.name} -> Child" 
        
    def info(self):
        return f"{self.name} is {self.age} years old"
        
subnode = SubNode("Krishna", 29)
print(subnode.greet())
print(subnode.info())

print("================================================================")

# Inheritance with **kwargs & *args

class SuperNode:
    def __init__(self, name):
        self.name = name 
        self.__example = "xyz"
        
    def greet(self):
        self.__welcome()
        return f"Hello, {self.name} -> Parent" 
        
    def __welcome(self):
        print("I say welcome")
        
class SubNode(SuperNode):
    def __init__(self, name, **kwargs):
        super().__init__(name)
        self.age = kwargs.get("age")
        
    def greet(self):
        print(super().greet())
        return f"Hello, {self.name} -> Child" 
        
    def info(self):
        return f"{self.name} is {self.age} years old" 
        
subnode = SubNode("Krishna", age=29)
print(SubNode.__mro__)
print(subnode.greet())
print(subnode.info())
print(SuperNode("Jack")._SuperNode__example)

print("=================================================================")
# Polymorphism

class AddNumber:
    def __init__(self, first):
        self.first = first
    def __add__(self, other):
        return AddNumber(self.first + other.first)
    def show(self):
        print(self.first)

a = AddNumber(1)
b = AddNumber(2)
c = a + b
c.show() # 3


print("===============================================================")
class Node:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __del__(self):
        print(f"Deleting object with name: {self}")

    @name.deleter
    def name(self):
        del self.__name

node = Node("krishna")
print(node.name)
node.name = "rohan"
print(node.name)
del node.name
print(node)
# print(node.name)

"""
krishna
rohan
<__main__.Node object at 0x7ba46fe17190>
Deleting object with name: <__main__.Node object at 0x7ba46fe17190>
"""
