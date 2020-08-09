#Python Program to understand Decorator_concept

def authenticate(a):
    uid=input("Enter username")
    passw=input("Enter password")
    if (uid == "admin" and passw == "admin"):
        print("Login successful")
        print("Enter into application requested")
    else:
        print("Login Failed")
        print("Can not enter into application requested")  
    return a

@authenticate
def application():
    pass

application()
