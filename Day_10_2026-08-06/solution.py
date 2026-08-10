full_name = input("Enter your full name: ")
email_address = input("Enter your email address: ")
country = input("Enter your country naem: ")
age = int(input("Enter your age: "))

name = full_name.strip()
name = name.title()
email_address = email_address.lower()

valid_name = ""
if len(name) < 3:
    valid_name = "Invalid Name"
else:
    valid_name = "Valid Name"

valid_email = ""
if "@" in email_address and "." in email_address:
    valid_email = "Valid Email"
else:
    valid_email = "Invalid Email"

format_country = country.title()

valid_age = ""
if age >= 13 and age <= 100:
    valid_age = "Valid Age"
else:
    valid_age = "Invalid Age"



if valid_name == "Valid Name" and valid_email == "Valid Email" and valid_age == "Valid Age":
    print("========== STUDENT REGISTRATION ==========")
    print()
    print(f"Name: {name}")
    print(f"Email: {email_address}")
    print(f"Country: {format_country}")
    print(f"Age: {age}")
    print()
    print("Status: Registration Sucessful")
    print()
    print("==========================================")
else: 
    if valid_name == "Invalid Name":
        print("========== INVALID NAME ==========")
        print()
        print(f"Name: {name}")
        print(f"Email: {email_address}")
        print(f"Country: {format_country}")
        print(f"Age: {age}")
        print()
        print("Status: Invalid Name")
        print()
        print("==========================================")
    elif valid_email == "Invalid Email":
        print("========== INVALID EMAIL ==========")
        print()
        print(f"Name: {name}")
        print(f"Email: {email_address}")
        print(f"Country: {format_country}")
        print(f"Age: {age}")
        print()
        print("Status: Invalid Email")
        print()
        print("==========================================")
    elif valid_age == "Invalid Age":
        print("========== INVALID AGE ==========")
        print()
        print(f"Name: {name}")
        print(f"Email: {email_address}")
        print(f"Country: {format_country}")
        print(f"Age: {age}")
        print()
        print("Status: Invalid Age")
        print()
        print("==========================================")


