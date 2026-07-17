#del keyword
class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("John")
print(s1.name)  # Output: John

del s1.name
#print(s1.name)


#private (like) attribute & methods
class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = account(12345, "password123")
print(acc1.acc_no)
print(acc1.reset_pass()) 


#inharitance    (single inharitance)
class car:
    color = "black"
    @staticmethod
    def start():
        print("car started...")


    @staticmethod
    def stop():
        print("car stoped...")

class toyotacar(car):
    def __init__(self, name):
        self.name = name

car1 = toyotacar("fortuner")
car2  = toyotacar("prius")

print(car1.start())
print(car2.start())



#multi -level inharitance
class car:
    color = "black"
    @staticmethod
    def start():
        print("car started...")


    @staticmethod
    def stop():
        print("car stoped...")

class toyotacar(car):
    def __init__(self, brand):
        self.brand = brand

class fortuner(toyotacar):
    def __init__(self, type):
        self.type = type  


car1 = fortuner("diesel")
car1.start()      



#multiple inharitance
class A:
    varA = 'welcome to class A'

class B:
    varB = 'welcome to class B'

class C(A, B):
    varC = 'welcome to class C'

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)




#super() method
class car:
    def __init__(self, type):
        self.type = type

        @staticmethod
        def start():
            print("car started...")

        @staticmethod
        def stop():
            print("car stoped...")


class toyotacar(car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)

car1 = toyotacar("prius", "diesel")
print(car1.type)



#class method   
class person:
    name = "anonymous"

    
    @classmethod
    def changename(cls, name):
        cls.name = name

p1 = person()
p1.changename("John")
print(p1.name)  
print(person.name) 



#property decorator
class student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"
    
stu1 = student(80, 90, 70)
print(stu1.percentage)

stu1.phy = 68
print(stu1.percentage)