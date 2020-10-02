#! python3

a=input("Enter a number smaller than 10: ")
a=int(a)

n=1
print("the sum of the series is ", end="")
for i in range(1,a+1):
    print(n,end="")
    n=n+1
    
    