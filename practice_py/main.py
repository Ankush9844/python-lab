
# girl = 9

# if girl > 21:
#     print("Yes, she can marry")

# elif(girl <= 18 ):
#     if girl == 18:
#         print("she should complete 12th first.")
#     elif(girl < 18 and girl > 10):
#         print("She is younger now")

#     else:
#         print("No comments")

# else:
#     print("She is small now, complete her education")

# ------------------------------------------
# import time

# my_time = time.strftime("%H-%M-%S")

# def average(*numbers):
#     print(type(numbers))
    
#     x = 0

#     for i in numbers:
#         x = x + i 

#     return x / len(numbers)

# print(average(1, 2, 3, 4))

# ------------------------------------------------------------

# try:
#     a = int(input("enter no: "))
#     for i in range(0, 10):
#         print (int(a*i))

# except Exception as e:ls

#     print(e)

# print("Hello")


# ----------------------------------------------------------


# import os

# if(not os.path.exists("data")):
# #     os.mkdir("data")

# folders = os.listdir("data")

# print(folders)

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))


# with open('index.txt', 'w') as f:
#     f.write("Hello world")

# lambda function

# double = lambda x: x*2
# avg = lambda x,y: (x+y)

# # def apply(a, b):
# #     return 6 + a(b)

# print(avg(double(10),20))
# # print(double(10))
# # print(apply(double, 3))


# # MAP #
# def cube(x):
#     return x**3

# l = [1,2,6,44,7,4,59,3]

# newl = []

# for item in l:
#     newl.append(cube(item))
# print(newl)


# newl = list(map(cube, l))
# print(newl)

# # FILTER #

# def filt_f(x):
#     return x>4

# newl = list(filter(filt_f, l))
# print(newl)

# class Person:
#     name = ""
#     occ = ""
#     networth = "" 

#     def info(self):
#         print(f"My name is {self.name} and i am {self.occ}")

        
# # self ka matlab wo object jiske liye method call kra jata he
# a = Person()

# a.info()

# b = Person()

# b.name = "Nikita"
# b.occ = "HR"

# b.info()

# # __init__
# class Person:

#     def __init__(self, n, o):
        
#         self.name = n
#         self.occ = o

#     def info(self):
#         print(f"My name is {self.name} and i am {self.occ}")

# a = Person("Harry", "Developer")
# b = Person("Nikita", "HR")

# a.info()
# b.info()

# # ------------------------------------
# class Person:
#     def __init__(self, n, a):
#         self.name = n
#         self.age = a

#     def detail(self):
        
#         print(f"My name is {self.name} and my age is {self.age}")

# # Creating a Person object
# person1 = Person("Alice", 30)

# person1.detail()

# # decorator

# class employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
#     @classmethod
#     def my_str(my_class, str):
#         return my_class(str.split("-")[0], str.split("-")[1])
    
# e1 = employee("Ankush", 28000)
# print(e1.name, e1.salary)


# str = "John-30000"
# e2 = employee.my_str(str)
# print(e2.name, e2.salary)

x = [1, 2]    
print(dir(x))