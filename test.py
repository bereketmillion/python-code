'''list=[2,"python"]
print(list)
list.append("hello world")
print(list)
list=[]
#x=int(input("Enter the number of elemnts you want to store: "))
for i in range(0,4):
#for i in range(x):
    list.append(input("Enter your elements: "))
print("printing the list items...")
#for i in list:
for i in range(4):
    print(list[i],end=" ")
x=eval(input("Enter the list: "))
s=sum(x)
print(s)
list=[3,6,"abebe",7]
#list.insert(2,88)
list.insert(-2,88)
print(list)
#index,count,len
n=[1,2,2,2,2,3,3]
print(n.index(3))
print(n.count(3))
print(len(n))
#extend
order1=["chicken","bread","fish"]
order2=["RC","KF","FO"]
order1.extend(order2) #order1=order1+order2
print(order1)
print(order2)
order=["chicken","mutton","fish"]
order.extend("mushroom") #order1=order1+order2
print(order)
#pop and remove
n=[10,20,30,20,40]
#print(n.pop())
#print(n.remove(20))
#print(n.remove(n[2]))
print(n)
#sort and reverse
n=[10,20,30,20,40]
n.sort()
#n.reverse()
print(n)
n.clear()
print(n)
#changing list to tuple
n=[10,20,30,20,40]
x=3,4,5,6,7
y=10,
t=tuple(n)
print(t)
print("n is ",type(t))
print("x is ",type(x))
print("y is ",type(y))
#operation on tuple
n=(10,20,30,20,40)
print(n.count(20))
print(n.index(30))
print(sorted(n))
print(len(n))
print(min(n))
print(maxn))
average=s(um/len(n)
print(average(n))


#this is  python program operation on set
s={12,2,3,4,5,6}
s.update(range(1,10,2),range(0,10,2))
print(s)
s1=s.copy()
print(s1)
s.pop()
print(s)
s.add("python")
print(s)
s.update("python")
s.remove(2)
print(s)
s.discard(12)
print(s)
s.clear()
print(s)


#this is python union intersection diference
x={2,3,4,5,6,10}
y={10,20,30,40}
#print(x.union(y))
print(x|y)#this is union
print(x&y)#this is intersection
print(x-y)#this is difference

#this is a python dictionary
f={"name":"bereket","age":21,"DPT":"IT","year":2024}
print(type(f))
print(f)
f["age"]=20
f["DPT"]='SE'
f["year"] =2025

print(f)
d={}
d[100]="karathi"
d[200]="becky"
d[300]="sri"
d['rgm']='nandyal'
print(d)
#second class
d={}
for i in range(5):
    name=input("Enter your name: ")
    mark=float(input("Enter your mark: "))
    d[name]=mark
for i in d:
    print(i,d[i])
#print(d)'''


# employee={"name":"deb","age":20,"salary":4500,"company":"WIPRO"}
# print(employee.get("salary"))
# employee.update({"salary":8000})
# employee["location"]="debrebirhan"
# employee.pop("age")
# print(employee.keys())
# list=employee.items()
# print(list)
# print(employee)

#using matplotlib
#from matplotlib import pyplot as plt
'''from matplotlib import pyplot as plt
x = ["USA","canada","Ethiopia","sudan","japan","England"]
y = [40,48,57,62,74,87]
plt.style.use("ggplot")
plt.plot(x,y)
plt.title("Line graph")
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()


#bar graph
from matplotlib import pyplot as plt
x = ["USA","canada","Ethiopia","sudan","japan","England"]
y = [40,48,57,62,74,87]
plt.bar(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Plot')
plt.show()


#scattered plot
from matplotlib import pyplot as plt
x = ["USA","canada","Ethiopia","sudan","japan","England"]
y = [98,48,57,102,74,87]
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Plot')
plt.show()

#histogram
import matplotlib.pyplot as plt
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()'''

# #file management
# x=open("C:/Users/Abr/Desktop/educational/python code/student.txt",'w')
# x.write("Information Technology") #we can write in the file also
# x.close()
# #r=open("C:/Users/Abr/Desktop/educational/python code/student.txt",'r')
# with open("C:/Users/Abr/Desktop/educational/python code/student.txt",'r') as y:
#     print(y.read())
# # x=r.read()
# # print(x)


# x=open("C:/Users/Abr/Desktop/educational/python code/student.txt",'w')
# x.write("information technology\n")
# x.write("information engineering\n")
# x.write("information system\n")
# x.write("information science\n")
# x.close()



# y=open("C:/Users/Abr/Desktop/educational/python code/student.txt",'r')
# # # for i in y:
# # #     print(i)
# print(y.readlines())
# # print(y.readline())
# y.close()


# # #operation on r+(read plus)
# x=open("C:/Users/Abr/Desktop/educational/python code/student.txt",'r+')
# # x.write("information technology")
# # x.write("information engineering")
# # x.write("information system")
# # x.write("information science")
# print(x.tell())
# x.write("computer")
# print(x.tell())
# print(x.read())
# print(x.tell())
# x.close()



# #operation on write plus
# x=open("C:/Users/Abr/Desktop/educational/python code/student.txt",'w+')
# #print(x.read())
# print(x.tell())
# x.write("information technology")
# print(x.tell())
# print(x.seek(12))
# print(x.tell())



# #a demo for error handling
# x = 5
# y = "hello"
# # w=x+y
# # print(w)
# try:
#     z = x + y
#     print(z)
# except TypeError:
#     print("Error: cannot add an int and a str")


#this demo for join operation
parts = ["hello", "world", "from", "Python"]
joined_string = " ".join(parts) # Join with spaces
print(joined_string)




# this is a demo for Python split() method
str = "Java is a programming language"
str2 = str.split()
print(str)
print(str2)

#lab exercise
#Information Technology
# def add_student_info():
#     student_id = input("Enter student ID: ")
#     name = input("Enter student name: ")
#     age = input("Enter student age: ")
#     with open("students.txt", "a") as file:
#         file.write(f"{student_id},{name},{age}\n")
#     print("Student information added successfully.")
# def search_student_by_id(student_id):
#     with open("students.txt", "r") as file:
#         for line in file:
#             info = line.strip().split(",")
#             if info[0] == student_id:
#                 return info
#     return None
# def retrieve_all_students():
#     with open("students.txt", "r") as file:
#         for line in file:
#             info = line.strip().split(",")
#             print(f"Student ID: {info[0]}, Name: {info[1]}, Age: {info[2]}")
# def update_student_info(student_id, new_name, new_age):
#     updated_info = []
#     with open("students.txt", "r") as file:
#         for line in file:
#             info = line.strip().split(",")
#             if info[0] == student_id:
#                 info[1] = new_name
#                 info[2] = new_age
#             updated_info.append(",".join(info))
#     with open("students.txt", "w") as file:
#         for updated in updated_info:
#             file.write(f"{updated}\n")
#     print("Student information updated successfully.")
# def delete_student_info(student_id):
#     filtered_info = []
#     with open("students.txt", "r") as file:
#         for line in file:
#             info = line.strip().split(",")
#             if info[0] != student_id:
#                 filtered_info.append(",".join(info))
#     with open("students.txt", "w") as file:
#         for filtered in filtered_info:
#             file.write(f"{filtered}\n")
#     print("Student information deleted successfully.")
# while True:
#     print("\n1. Add Student\n2. Search Student\n3. Retrieve All Students\n4. Update Student\n5. Delete Student\n6. Exit")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         add_student_info()
#     elif choice == "2":
#         student_id = input("Enter student ID to search: ")
#         student_info = search_student_by_id(student_id)
#         if student_info:
#             print(f"Student found - ID: {student_info[0]}, Name: {student_info[1]}, Age: {student_info[2]}")
#         else:
#             print("Student not found.")
#     elif choice == "3":
#         retrieve_all_students()
#     elif choice == "4":
#         student_id = input("Enter student ID to update: ")
#         new_name = input("Enter new name: ")
#         new_age = input("Enter new age: ")
#         update_student_info(student_id, new_name, new_age)
#     elif choice == "5":
#         student_id = input("Enter student ID to delete: ")
#         delete_student_info(student_id)
#     elif choice == "6":
#         break
#     else:
#         print("Invalid choice. Please try again.")
# student_id = input("Enter student ID: ")
# name = input("Enter student name: ")
# age = input("Enter student age: ")
# print(f"hollo,{student_id},{name},{age}\n")

