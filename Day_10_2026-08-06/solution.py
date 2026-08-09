full_name = input("Enter your full name: ")
email_address = input("Enter your email address: ")
country = input("Enter your country naem: ")
age = int(input("Enter your age: "))

name = full_name.strip()
name = name.title()
email_address = email_address.lower()

validate_name = ""
if len(name) < 3:
    validate_name = "Invalid Name"
else:
    validate_name = "Valid Name"

validate_email = ""
if "@" in email_address and "." in email_address:
    validate_email = "Valid Email"
else:
    validate_email = "Invalid Email"

format_country = country.title()

validate_age = ""
if age >= 13 and age <= 100:
    validate_age = "Valid Age"
else:
    validate_age = "Invalid Age"



if validate_name == "Valid Name" and validate_email == "Valid Email" and validate_age == "Valid Age":
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
    if validate_name == "Invalid Name":
        print("========== STUDENT REGISTRATION ==========")
        print()
        print(f"Name: {name}")
        print(f"Email: {email_address}")
        print(f"Country: {format_country}")
        print(f"Age: {age}")
        print()
        print("Status: Invalid Name")
        print()
        print("==========================================")
    elif validate_email == "Invalid Email":
        print("========== STUDENT REGISTRATION ==========")
        print()
        print(f"Name: {name}")
        print(f"Email: {email_address}")
        print(f"Country: {format_country}")
        print(f"Age: {age}")
        print()
        print("Status: Invalid Email")
        print()
        print("==========================================")
    elif validate_age == "Invalid Age":
        print("========== STUDENT REGISTRATION ==========")
        print()
        print(f"Name: {name}")
        print(f"Email: {email_address}")
        print(f"Country: {format_country}")
        print(f"Age: {age}")
        print()
        print("Status: Invalid Age")
        print()
        print("==========================================")


