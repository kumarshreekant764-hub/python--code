# class Student :
#     name = "karan kumar"
#     age = 20

# s1 = Student()
# print(s1.name)
# print(s1.age)


# class Car :
#     model = "BMW"
#     color = "Black"
#     brand = "BMW"
    
# c1 = Car()
# print(c1.model)
# print(c1.color)
# print(c1.brand)


#__init__ function is a constructor in python. It is used to initialize the object of a class. It is called automatically when an object of a class is created. The __init__ function is defined using the def keyword and it takes at least one argument, self, which refers to the instance of the class.
# class Student:
#    def __init__(self, fullname, age):
#       self.name = fullname
#       self.age = age
#       print("Student object created")

# s1 = Student("karan kumar", 20)
# print(s1.name)
# print(s1.age)

# s2 = Student("rahul kumar", 22)
# print(s2.name)
# print(s2.age)

#oop methods
class Student:
   college_name = "ABC College"

   def __init__(self, fullname, age):
      self.name = fullname
      self.age = age

   def welcome(self):
      print("welcome to ABC College", self.name)

   def get_age(self):
      return self.age

s1 = Student("karan kumar", 20)
s1.welcome()
print(s1.get_age())


#static method______
class Student:
   college_name = "ABC College"

   def __init__(self, fullname, age):
      self.name = fullname
      self.age = age

   @staticmethod
   def welcome():
      print("welcome to ABC College")

s1 = Student("karan kumar", 20)
s1.welcome()
print(Student.college_name)
print(s1.name)
print(s1.age)



#create Account class with 2 attributes - balance & account no. 
# create methods for debit , credit & printing the balance. 

class Account:
    def __init__(self, bal, acc_no):
         self.balance = bal
         self.account_no = acc_no

      #debit method
    def debit(self, amount):
       self.balance -= amount
       print("Rs.", amount, "was debited")
       print("Current balance is Rs.", self.balance)

    #credit method
    def credit(self, amount):
       self.balance += amount
       print("Rs.", amount, "was credited")
       print("Current balance is Rs.", self.balance)


    def get_balance(self):
       return self.balance

acc1 = Account(1000, 123456789)
acc1.debit(500)
acc1.credit(200)
acc1.credit(3000)