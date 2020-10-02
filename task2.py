#! python3


a=input("Enter a name: ")
name=("Lebron", "Kobe", "Michael", "Shaq", "Dennis")

for i in name:
    if a==i:
         print("That name is on the list")
         break
    
else:
 print("That name is not on the list")
            
