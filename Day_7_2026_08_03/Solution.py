customer_fullname = input("Enter your full name: ")
customer_age = int(input("Enter your age: "))
accompanied = input("Does you accompained by a parents (Yes / No): ")
status = " "

if customer_age >= 18:
    status = "allowed"
else:
    if customer_age < 18 and (accompanied.lower()) == "yes":
        status = "allowed with parents"
    else:
        status = "not allowed"

if status == "not allowed":
    print("========== MOVIE TICKET ==========")
    print()
    print(f"Customer: {customer_fullname}")
    print(f"Age: {customer_age}")
    print()
    print(f"Parent Present: {accompanied}")
    print()
    print(f"Status: {status}")
    print()
    print("==================================")
elif status == "allowed with parents":
    print("========== MOVIE TICKET ==========")
    print()
    print(f"Customer: {customer_fullname}")
    print(f"Parent Present: {accompanied}")
    print()
    print(f"Status: {status}")
    print()
    print("==================================")
else:
    print("========== MOVIE TICKET ==========")
    print()
    print(f"Customer: {customer_fullname}")
    print(f"Age: {customer_age}")
    print()
    print(f"Parent Present: {accompanied}")
    print()
    print(f"Status: {status}")
    print()
    print("==================================")
