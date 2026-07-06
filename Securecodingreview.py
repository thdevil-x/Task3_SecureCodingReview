# vulnerable_login.py

# Hardcoded username and password
USERNAME = "admin"
PASSWORD = "admin123"

print("=== Login System ===")

username = input("Enter Username: ")
password = input("Enter Password: ")

# Plain text password comparison
if username == USERNAME and password == PASSWORD:
    print("Login Successful!")
else:
    print("Invalid Username or Password")