import os

# Hardcoded password (security vulnerability)
PASSWORD = "123456"

# Unused variable (code smell)
temp_variable = 42

def insecure_function():
    # Command injection vulnerability
    filename = input("Enter filename to delete: ")
    os.system("rm -rf " + filename)  # BAD PRACTICE

# Bug: Logic error (comparison mistake)
def check_age(age):
    if age = 18:  # should be '=='
        print("You are 18!")
