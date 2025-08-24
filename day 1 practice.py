user_name=input("Enter user name:")
password=int(input("Enter password:"))
if user_name=="sathya":
    print("correct username")
    if password==1234:
        print("correct password")
    else:
        print("Wrong password")    
else:
    print("Wrong username")      