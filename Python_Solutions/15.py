def validation (user,password):
    if user =="admin" and password == "pass123":
        print("Login successful!")
    elif user != "admin":
        print("Invalid username.")
    elif password != "pass123":
        print("Invalid password.")
    else:
        print("Invalid username and password.")
user = "admin"
password = "pass123"
validation(user,password)