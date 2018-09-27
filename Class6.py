#FUNCTIONS

#Que1
print("calculate area of sphere")
def area_of_sphere():
    r = int(input("enter radius : "))
    pi = 3.14
    area = 4*pi*r*r
    print("surface area of sphere : ", area)
area_of_sphere()
print("\n")

#Que2
print("perfect numbers from 1 to 1000")
list = []
def perfect_num(n):
    for i in range(1,1000):
        for i in range(1,n+1):
            if n % i == 0:
                list.append(i)
        sum = 0
        for i in list:
            sum +=i
        if (sum/2) == n:
            print(n, "is a perfect number")    
        list.clear() 
        n = n+1
perfect_num(1)
print("\n")

#Que3
print("table of an integer n")
n = int(input("enter an integer : "))
print("TABLE OF", n)
for i in range(1,11):
    print(n,"*",i,"=",n*i)
print("\n")

#Que4
print("recursive function to calculate power of function")
def power_of_number(a,b):
    if(b == 1):
        return(a)
    else:
        return(a*power_of_number(a,b-1))
base = int(input("enter the number : "))
exp = int(input("enter the power to be raised : "))
power = power_of_number(base,exp)
print(base, "raised to" , exp , " : " , power)
