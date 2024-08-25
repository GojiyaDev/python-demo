#problem solving
#1  write a program to check if a number is positive

number = 0
if number > 0:
    print("Number is Positive")
elif number < 0:
    print("Number is Negetive")
else:
    print("Number is Zero")


#2 write a program to check whether a number is odd or even

number = 150
if number %2==0:
    print("Number is Even")
else:
    print("Number is Odd")


#3 write a program to create area calculator

print("*************--> AREA CALCULATOR <--*************")
print('''Press 1 to get the area of Square
Press 2 to get the area of Recetangle
Press 3 to get the area of Circle
Press 4 to get the area of Triangle''')

choice = int(input("Enter A number between 1-4 :"))
if choice == 1:
    side = float(input("Enter the length of one side :"))
    area = side**2
    print("the area of sqaure is ", area)
elif choice == 2:
    length = float(input("Enter Length of the rectangle : "))
    width = float(input("Enter the width of the rectangle : "))
    area = length*width
    print("The area of rectangle is : ", area)
elif choice == 3:
    radius = float(input("Enter the raduis of circle : "))
    area = ((22/7)*(radius**2))
    print("the area of circle is ", area)

elif choice == 4:
    base = float(input("Enter the base of the triangle :"))
    height = float(input("Enter the height of the triangle :"))
    area = 0.5*base*height
    print("the area of triangle is ", area)
else:
    print("Invalid Input")


#4 wite a program check whether the passed letter is vowel or not

char = input("Enter Single Character : ")
if char.lower == 'a e i o u':
    print("Enter Character is Vowel")
else:
    print("Enter Character is Not Vowel")


#5 write a program to check if a number is a single digit number, 2 digit number and so on...., upto 5 digits

number = input("Enter A Number : ")
lenght = len(number)
if lenght == 1:
    print("Number is One Digit")
elif lenght == 2:
    print("Number is Two Digit")
elif lenght == 3:
    print("Number is Three Digit")
elif lenght == 4:
    print("Number is Four Digit")
elif lenght == 5:
    print("Number is Five Digit")
else:
    print("Number is have More for than Five Digits")
