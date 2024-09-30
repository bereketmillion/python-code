# list=[2,"python"]
# print(list)
# list.append("hello world")
# print(list)



# list=[]
# #x=int(input("Enter the number of elements you want to store: "))
# for i in range(0,4):
# #for i in range(x):
#     list.append(input("Enter your elements: "))
# print("printing the list items...")
# #for i in list:
# for i in range(4):
#     print(list[i],end=" ")



###insert
# x=eval(input("Enter the list: "))
# s=sum(x)
# print(s)
# list=[3,6,"abebe",7]
# #list.insert(2,88)
# list.insert(-2,88)
# print(list)


###index,count,len
# n=[1,2,2,2,2,3,3]
# print(n.index(3))
# print(n.count(3))
# print(len(n))


###extend
# order1=["chicken","bread","fish"]
# order2=["RC","KF","FO"]
# order1.extend(order2) #order1=order1+order2
# print(order1)
# print(order2)
# order=["chicken","mutton","fish"]
# order.extend("mushroom") #order1=order1+order2
# print(order)



###pop and remove
#n=[10,20,30,20,40]
#n.pop()
#print(n.pop())
#print(n.remove(20))
# print(n.remove(n[2]))
# print(n)



###sort and reverse
# n=[10,20,30,20,40]
# n.sort()
# print(n.reverse())
# print(n)
# n.clear()
# print(n)



###changing list to tuple
# n=[10,20,30,20,40]
# x=3,4,5,6,7
# y=10,
# t=tuple(n)
# print(t)
# print("n is ",type(t))
# print("x is ",type(x))
# print("y is ",type(y))



###operation on tuple
# n=(10,20,30,20,40)
# print(n.count(20))
# print(n.index(30))
# print(sorted(n))
# print(len(n))
# print(min(n))
# print(max(n))
# average=sum/len(n)
# print(average(n))


# #this is  python program operation on set
# s={12,2,3,4,5,6}
# s.update(range(1,10,2),range(0,10,2))
# print(s)
# s1=s.copy()
# print(s1)
# s.pop()
# print(s)
# s.add("python")
# print(s)
# s.update("python")
# s.remove(2)
# print(s)
# s.discard(12)
# print(s)
# s.clear()
# print(s)



# #this is python union intersection diference
# x={2,3,4,5,6,10}
# y={10,20,30,40}
# #print(x.union(y))
# #print(x|y) #this is union
# print(x.union(y)) #this is union
# #print(x&y) #this is intersection
# print(x.intersection(y)) #this is intersection
# #print(x-y) #this is difference
# print(x.difference(y))


#this is a python dictionary
# f={"name":"bereket","age":21,"DPT":"IT","year":2024}
# print(type(f))
# print(f)
# f["age"]=20
# f["DPT"]='SE'
# f["year"] =2025
#
# print(f)
# d={}
# d[100]="karathi"
# d[200]="becky"
# d[300]="sri"
# d['rgm']='nandyal'
# print(d)

###                        This preparation for exam

# lists =[] #Declaring the empty
# for i in range(0,4):
#  lists.append(input("Enter the item:"))
# print("printing the list items..")
# for i in lists:
#  print(i,end=" ")

# n=[1,5,3,4]
# print(n.sort())
# print(n)


###tuple
# list=[10,20,30]
# t=tuple(list)
# print(t)
# print(type(t))


# x=(2023, 56, 3.11, 8, 22,8)
# print(x.count(8))
# print(x[3])
# print(x.index(8))
# print(sorted(x))
# print(min(x))
# print(max(x))
#
# y=(a,b,c)
# print(sorted(x))


# d=dict({100:"karthi",200:"saha"})
# print(d)
# d=dict([(100,"karthi"),(200,"saha"),(300,"sri")])
# print(d)
# d=dict(((100,"karthi"),(200,"saha"),(300,"sri")))
# print(d)
# d=dict({(100,"karthi"),(200,"saha"),(300,"sri")})
# print(d)
# d=dict(({100,"karthi"},{200,"saha"},{300,"sri"}))
# print(d)
# #d=dict({[100,"karthi"],[200,"saha"],[300,"sri"]})
# print(d)
# print(len(d))



# Employee = {"Name": "Dev", "Age":
# 20,"salary":45000,"Company":"WIPRO"}
# print(Employee.get("salary"))


# d={100:"karthi",200:"sahasra",300:"sri"}
# print(d)
# d.clear()
# print(d)

# Employee = {"Name": "Dev", "Age": 20, "salary":45000,"Company":"WIPRO"}
# Employee.update({"salary":8000})
# print(Employee)



# Employee = {"Name": "Dev", "Age":
# 20,"salary":45000,"Company":"WIPRO"}
# Employee.pop("Age")
# print(Employee)


# d={100:"hana",200:"abebe",300:
# "elsa"}
# print(d)
# print(d.popitem())
# print(d)


# d={100:"hana",200:"sosi",300:"kebede"}
# print(d.keys())
# print(d.values())



# d={100:"hana",200:"sosi",300:"kebede"}
# list = d.items()
# print(list)


