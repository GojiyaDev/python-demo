#1 Write a program to find a sum of all the even up to 50

sum = 0
for i in range(2,51,2):
    sum += i
print(sum)


#2 write a program to write first 20 numbers and their squared number

sum = 0 
for i in range(1,21):    
    print(" ")
    sum = i
    i *=i
    print(sum,i, end=" ")
    i=0


#3 write a program to find sum of first 10 odd numbers usinf while loop

n = 1
sum = 0
while n<=20:
    if n %2== 1:
        sum +=n       
    n +=1
print(sum)



#4 write a program to check if a number is divisible by 8 and 12 to 100 numbera

for i in range(1,101):
    if i%8 == 0 and i%12==0:
        print(i)


#5 write a program to create a billing system at supermarket

while True:
    
    name = input("Enter Customer's name : ")
    total = 0
    
    while True:
        print("Enter the amount and qua")
        amount = float(input("Enter Amount : "))
        qua = float(input("Enter Quantity : "))
        total += amount * qua
        repeat = input("Do you want to add more items ? (Yes/No) : ")
    
        if repeat == "No" or repeat == "no":
            break
    
    print("--" *40)
    print("Name : ",name)
    print("Amount to be paid: ",total)
    print("--" *40)
    print("*************** Happy Shopping ***************")
    
    repeat1 = input("Do you want to go to next customer ? (yes/no): ")
    
    if repeat1 == "No" or repeat1 == "no":
        break

