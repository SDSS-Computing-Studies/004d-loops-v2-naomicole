#! python3


a=input("Enter a name: ")
name=("Lebron", "Kobe", "Michale", "Shaq", "Dennis")

for i in name:
    if a==i:
        print("That name is on the list")
        break
    
else:
 print("That name is not in the list")
            
