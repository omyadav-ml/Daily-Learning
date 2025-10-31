# Password Authentication using python
# It Capture invisible key sequence 🔑


import getpass

database={
    "Agent_Om":"Agent8282",
    "Om.Victus":"om@7400"
}

username=input("Enter Your Username: ")

if username in database:
    password= getpass.getpass("Enter Your Password: ")

    while password != database[username]:
        print("Incorrect password. Try again! ")
        password = getpass.getpass("Enter Your Password Again: ")

    print("Verifed Login Successfully.")
else:
    print("Username not found. Please check and try again.")

