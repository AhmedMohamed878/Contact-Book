contacts= dict(Ahmed="01000406933",Ali="0029501-01939", Dona="00284789747")
print(contacts)

name=str(input("Enter the name: "))
number = contacts.get(name)
    
if name in contacts:    
    print("The phone number of: " + name + " is " + number)
  
else:
        print("Invalid name")
