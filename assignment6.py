'''
#Question1:->Create a function to calculate the area of a sphere by taking radius from user.
'''
def area_sphere(n):
    pi=3.14
    temp=4*pi*n*n
    return temp
r=int(input("Enter radius: "))
output=area_sphere(r)
print("The area of sphere is :",output)
print()

'''
#Question2:->Write a function “perfect()” that determines if parameter number is a perfect number.
 Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself),
 sum to the number. E.g., 6 is a perfect number because 6=1+2+3]. 
'''
def perfect(num):
    result=0
    temp=num
    for i in range(1,num):
        if (num%i==0):
            result=result+i
    if (result==temp):
        print(temp)
for i in range(1,1001):
    perfect(i)
print()

'''
#Question3:->Print multiplication table of n using loops, where n is an
integer and is taken as input from the user.
'''
def table(num):
    for i in range (1,11):
        temp=num*i
        print(num,'*',i,"=",temp)
num1=int(input("enter the value of table: "))
table(num1)
print()

'''
#Question4:->Write a function to calculate power of a number
raised to other ( a^b ) using recursion.
'''
def power(a,b):
    num2=a
    if b==0:
        return a/a
    else:
        return(a*power(a,b-1))  
value=int(input("Enter number : "))
power1=int(input("Enter power: "))
print(power(value,power1))



