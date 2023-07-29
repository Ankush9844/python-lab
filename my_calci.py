# Hello, My name is Ankush. And this repo is only for demo purpose, I just made the calculator app only fo rdummy purpose

def addition(First_no, Second_no):
    return(First_no + Second_no)
def subtraction(First_no, Second_no):
    return(First_no - Second_no)
def division(First_no, Second_no):
    return(First_no / Second_no)
def multiplication(First_no, Second_no):
    return(First_no * Second_no)

select = input(" Take 1 for addition \
               Take 2 for subtraction, \
               division 3, \
               multiplication 4 \
               : ")

x = int(input("enter value of x : "))
y = int(input("enter value of y : "))

if select == "1" :
    print(x, "+" , y, "=", addition(x, y))
    
elif select == "2" :
    print(x, "-" , y, "=", subtraction(x, y))
elif select == "3" :
    print(x, "/" , y, "=", division(x, y))
elif select == "4" :
    print(x, "*" , y, "=", multiplication(x, y))

else: 
    print("Invalid input! sorry try again")


