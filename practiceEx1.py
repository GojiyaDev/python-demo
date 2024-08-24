#problems Ex1
# 1 write a program to display a person's name, age and address in three different lines

name = "Dev Gojiya"
print(name)
age = 21
print(age)
address = "UPES Bidholi Campus"
print(address)

# 2 write a program to swap two variables

a = 10
b = 20

print("Before Swapping : ",a,b)
temp = a
a = b
b = temp
print("After Swapping : ",a,b)

# 3 write a program to convert a flaot into integer

a = 10.12
print("before converstion : ",type(a))
a = int(a)
print("after Converstion : ", type(a))

# 4 write a program to take details from a student for ID-card and then print it in different lines.

Name = input("Enter Your Full Name : ")
dep = input("Enter Your Depertment : ")
program = input("Enter Your Program Name : ")
batch = input("Enter Your Batch Number : ")
BOD = input("Enter Your Birth Date : ")

print(Name,"//",dep,"//",program,"//",batch,"//",BOD )

# 5 write a program to take an user input as integer then convert to flaot

number  = int(input("Enter Any Random Number :"))
print("Before coversion",type(number))
number = float(number)
print("After converstion value is :",number)
print("After converstion", type(number))

#conditional statement
#if the Statement

marks = 70
if marks >= 90:
    print("you will get mobile phone")
print("thank you")

#if else statement

marks = 70
if marks >= 90:
    print("you will get new mobile phone")
else:
    print("Better luck next time")


