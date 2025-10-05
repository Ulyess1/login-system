def Registration():
    username = input("Enter Username :")
    password = input("Enter Password :")
    record = {"Name":username , "pass":password}
    login.append(record)
    print("Account Registered Successfully.")
def Login():
    user = input("Enter Username :")
    pas = input("Enter Password :")
    isFound=False
    for i in login:
        if user==i["Name"] and pas==i["pass"]:
            isFound = True
            print("Logged in successfully.")
            break
        if isFound==False:
            print()
            print("Username or password incorrect.")
login = []

while True:
    print("1- Registration :")
    print("2- Login :")
    print("3- Exit :")
    choice = int(input("Select Your choice : "))

    if choice == 1:
        print()
        print("Registration Section :")
        Registration()
    elif choice == 2:
        print()
        print("Login Section :")
        Login()
    elif choice == 3:
        print()
        print("Good Bye..")
        break
    else:
        print("Invalid Choice..")
        break
