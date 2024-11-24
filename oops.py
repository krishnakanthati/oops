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