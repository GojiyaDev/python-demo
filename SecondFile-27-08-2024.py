# 27-08-2024 time 3:00 to 3:55 in 4001
# if block
a=10
b=1
if a > b:
    print("A > B")
    print("this condition is true")
if a < b:
    print("A < B")
    print("this condition is true")
if a == b:
    print("A == B")
    print("this condition is true")
if a != b:
    print("A != B")
    print("this condition is true")


# And, OR, Not operator
a = 100
b = 2
c = 30

if a > b and a > c:
    print("A is Largest")
elif b > a and b > c:
    print("B is Largest")
else:
    print("C is Largest")

#function can be use multiple time 
""" 
def is short for definition
"""

def myprint(inputvar):
    a=inputvar
    print(f"value is {a}")
    print(f"id is {id(a)}")
    print(f"Type is {type(a)}")

myprint(10)
myprint(1)
myprint(100)

#write a program user input first name and last name and great with like hii user and his name should be upper case

firstname = input("Enter Your First Name :")
lastname = input("Enter Your Last Name : ")

firstname = firstname.capitalize()
lastname = lastname.capitalize()

fullname = "Hello "+firstname +" "+ lastname
print(fullname)


while True:
    try:        
        number = int(input("Enter an integer: "))
        break  
    except ValueError:
        
        print("Invalid input. Please enter a valid integer.")


print(f"\n Multiplication Table for {number}:")
for i in range(1, 11): 
    result = number * i
    print(f"{number} x {i} = {result}")
