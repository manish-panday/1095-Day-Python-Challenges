full_name = input("Enter your name: ")
marks = int(input("Enter your marks (0-100): "))

if marks >= 40:
    if marks >= 90:
        print("Outstanding Performance")
    status = "Pass"
    print("========== RESULT ==========")
    print()
    print(f"Student: {full_name}")
    print(f"Mark: {marks}")
    print(f"Status: {status}")
    print("==========================")
else:
    status = "Fail"
    print("========== RESULT ==========")
    print()
    print(f"Student: {full_name}")
    print(f"Mark: {marks}")
    print(f"Status: {status}")
    print("===========================")

#Done it's work better....