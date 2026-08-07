student_fullname = input("Enter your full name. ")
library_mamber = input("Are you a library mamber? (yes/no): ")
overdue = input("Do you have any oveerdue books? (yes/no): ")
status = " "

if library_mamber.lower() == "no":
    status = "MamberShip required"
else:
    if overdue.lower() == "no":
        status = "Allowed"
    else:
        status = "Return Overdue Book"

if status == "MamberShip required":
    print("========== LIBRARY STATUS ==========")
    print()
    print(f"Student: {student_fullname}")
    print()
    print(f"Library Member: {library_mamber}")
    print(f"Overdue Books: {overdue}")
    print()
    print(f"Status: {status}")
    print()
    print("===================================")
elif status == "Return Overdue Book":
    print("========== LIBRARY STATUS ==========")
    print()
    print(f"Student: {student_fullname}")
    print()
    print(f"Library Member: {library_mamber}")
    print(f"Overdue Books: {overdue}")
    print()
    print(f"Status: {status}")
    print()
    print("===================================")
else:
    print("========== LIBRARY STATUS ==========")
    print()
    print(f"Student: {student_fullname}")
    print()
    print(f"Library Member: {library_mamber}")
    print(f"Overdue Books: {overdue}")
    print()
    print(f"Status: {status}")
    print()
    print("===================================")


#Done !!!!

