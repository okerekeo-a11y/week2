"""
Ogechukwu Okereke
CSMC 111
Spring 2026
week2 assignment4
"""
correct_username = "admin"
correct_password = "password123"
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Login failed. Incorrect username or password.")