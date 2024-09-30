#this is demo for object oriented programming
# class circle:
#     pie=3.14
#     def __init__(self,r):
#         self.radius=r
#     def ac(self):
#         print("area of the circle is ",self.pie*(self.radius*self.radius))
#     def cc(self):
#         print("parameter of the circle is ",2 * self.pie * self.radius)
# x=int(input("Enter the radius: "))
# c1=circle(x)
# c2=circle(x)
# c1.ac()
# c2.cc()



#inheritance
# class operation:
#     def __init__(self,num1,num2):
#         self.number1=num1
#         self.number2=num2
#     def add(self):
#         print("the sum of the numbers is: ",self.number1 + self.number2)
#         print("the difference of the numbers is: ", self.number1 - self.number2)
# class op1(operation):
#     def mult(self):
#         print("the multiplication of the numbers is: ", self.number1 * self.number2)
#         print("the division of the numbers is: ", self.number1 / self.number2)
# x=int(input("Enter the first number: "))
# y=int(input("Enter the second number: "))
# # obj1=operation(x,y)
# # obj1.add()
# #obj1.mult()     #genarate error
# obj2=op1(x,y)
# obj2.add()
# obj2.mult()



#super
# class operation:
#     def __init__(self,num1,num2):
#         self.number1=num1
#         self.number2=num2
#     def add(self):
#         print("the sum of the numbers is: ",self.number1 + self.number2)
#         print("the difference of the numbers is: ", self.number1 - self.number2)
# class op1(operation):
#     def __init__(self,num1,num2,num3):
#         super().__init__(num1, num2)
#         self.number3=num3
#     def mult(self):
#         print("the multiplication of the numbers is: ", self.number1 * self.number2*self.number3)
#         print("the division of the numbers is: ", self.number1 / self.number2/self.number3)
# x=eval(input("Enter the first number: "))
# y=eval(input("Enter the second number: "))
# z=eval(input("Enter the third number: "))
# obj2=op1(x,y,z)
# #obj2.mult()
# obj2.add()
# obj2.mult()



#there is one left multilevel inheritance
#multiple inheritance
# class grandmother:
#     def __init__(self,num1,num2):
#         self.number11=num1
#         self.number22=num2
#     def add(self):
#         print("the sum of the numbers is: ",self.number1 + self.number2)
# class mother(grandmother):
#     def __init__(self, num1, num2):
#         self.number1 = num1
#         self.number2 = num2
#     def sub(self):
#         print("the difference of the numbers is: ", self.number1 - self.number2)
# class child(mother):
#     def mult(self):
#         print("the multiplication of the numbers is: ", self.number1 * self.number2)
#         print("the division of the numbers is: ", self.number1 / self.number2)
# x=int(input("Enter the first number: "))
# y=int(input("Enter the second number: "))
# obj2=child(x,y)
# obj2.add()
# obj2.sub()
# obj2.mult()



#herarchial inhereitance
#hybrid inheritance
# class grandmother:
#     def __init__(self,num1,num2):
#         self.number11=num1
#         self.number22=num2
#     def add(self):
#         print("the sum of the numbers is: ",self.number1 + self.number2)
# class mother(grandmother):
#     def __init__(self, num1, num2):
#         self.number1 = num1
#         self.number2 = num2
#     def sub(self):
#         print("the difference of the numbers is: ", self.number1 - self.number2)
# class father(grandmother):
#     def __init__(self,num3,num4):
#         self.number1=num3
#         self.number2=num4
#     def mult(self):
#             print("the multiplication of the numbers is: ", self.number1 * self.number2)
# class child(mother,father):
#     def div(self):
#         print("the division of the numbers is: ", self.number1 / self.number2)
# x=int(input("Enter the first number: "))
# y=int(input("Enter the second number: "))
# obj2=child(x,y)
# obj2.add()
# obj2.sub()
# obj2.mult()
# obj2.div()


#polymorphism
#method overloading left
#method overriding
# class mother():
#     def __init__(self, num1, num2):
#         self.number1 = num1
#         self.number2 = num2
#     def add(self):
#         print("the sum of the numbers is: ", self.number1 + self.number2)
# class child(mother):
#
#     def add(self):
#         print("the difference of the numbers is: ", self.number1 - self.number2)
# x=int(input("Enter the first number: "))
# y=int(input("Enter the second number: "))
# obj1=child(x,y)
# obj1.add()




#operator overloading
# print(2+2)
# print("python"+"programmming")




#abstraction
# from abc import ABC,abstractmethod
# class operation(ABC):#object cannot be created byb abstract class
#     abstractmethod
#     def add(self,x,y):
#         pass
#     abstractmethod
#     def sub(self, x, y):
#         pass
#     abstractmethod
#     def mult(self, x, y):
#         pass
#     abstractmethod
#     def div(self, x, y):
#         pass
# class imp(operation):
#     def add(self, x, y):
#         print(x+y)
#     def sub(self, x, y):
#         print(x-y)
#     def mult(self, x, y):
#         print(x*y)
#     def div(self, x, y):
#         print(x/y)
# do=imp()
# do.add(2,1)
# do.sub(2,1)
# do.mult(2,1)
# do.div(2,1)
#does=operation()
#does.add(2,1)




#encapsulation
# class operation:
#     def __init__(self,x,y):
#         self.__num1=x
#         self.__num2=y
#     def add(self):
#         print(self.num1+self.num2)
# class op1(operation):
#     def sub(self, x, y):
#         print(self.num1-self.num2)
# ob=op1(5,3)
# ob.add()
# ob.sub(5,3)




#                            preparation for exam
# class operation:
#     def __init__(self,l,w):
#         self.length=l
#         self.width=w
#     def add(self):
#         print("the sum of the numbers is ",(self.length + self.width))
#     def sub(self):
#         print("the difference of the numbers is ", (self.length - self.width))
#     def mult(self):
#         print("the multiplication of the numbers is ",(self.length * self.width))
#     def div(self):
#         print("the division of the numbers is ",(self.length / self.width))
# person1 = operation(4,2)
# person1.add()
# person1.sub()
# person1.mult()
# person1.div()




# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#             print("Hello, my name is ",self.name,"\t",self.age)
# person1 = student("abebe", 25)
# person2 = student("alemu", 22)
# person3 = student("hana", 20)
# person1.greet()
# person2.greet()
# person3.greet()



# class calcu:
#     def __init__(self,num1,num2):
#         self.number1=num1
#         self.number2=num2
#     def suub(self):
#         print(self.number1-self.number2)
# class add(calcu):
#     def __init__(self, num1, num2,num3):
#         super().__init__(num1, num2)
#         self.number3=num3
#     def sub(self):
#         print(self.number1+self.number2+self.number3)
# a=add(10,3,9)
# a.sub()



# class art:
#     def __init__(self,num1,num2):
#         self.number1=num1
#         self.number2=num2
#     def operation(self):
#         print(self.number1+self.number2)
#         print(self.number1-self.number2)
# class atr1(art):
#     def __init__(self,num1,num2):
#         self.number1=num1
#         self.number2=num2
#     def operation(self):
#         print(self.number1*self.number2)
#         print(self.number1/self.number2)
# ob1=art(3,2)
# ob1.operation()


#Overloading in python


class complex_1:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    def __add__(self, U):
        return self.X + U.X, self.Y + U.Y
Object_1 = complex_1(23, 12)
Object_2 = complex_1(21, 22)
Object_3 = Object_1 + Object_2
print(Object_3)