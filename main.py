
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


# import time

# my_time = time.strftime("%H-%M-%S")

def average(*numbers):
    print(type(numbers))
    
    x = 0

    for i in numbers:
        x = x + i 

    return x / len(numbers)

print(average(1, 2, 3, 4))


try:
    a = int(input("enter no: "))
    for i in range(0, 10):
        print (int(a*i))

except Exception as e:
    print(e)

print("Hello")