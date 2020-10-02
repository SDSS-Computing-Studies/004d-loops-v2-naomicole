#! python3

w=input("Enter the width of the box: ")
w=int(w)
h=input("Enter the height of the box: ")
h=int(h)
h=h+1

for i in range (1,h):
    print("*"*w)
