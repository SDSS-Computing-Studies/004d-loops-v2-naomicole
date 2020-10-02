#! python3

n=input("Enter a number: ")
n=int(n)
b=0
c=1

for i in range(0,n):
    b=n-i
    c=b*c

print(str(n)+"! is "+str(c)+ " where "+str(n)+" is the integer entered and "+str(c)+ " is the calculated answer")
