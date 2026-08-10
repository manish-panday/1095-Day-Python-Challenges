number = int(input("Enter a number: "))

type = ""
if number > 0:
    type = "Positive"
elif number < 0:
    type = "Negative"
else:
    type = "Zero"


status = ""
if number % 2 == 0:
    status = "Even"
elif number  == 0:
    status = "Even"
else:
    status = "Odd"

flag = ""
if number % 5 == 0:
    flag = "Yes"
else:
    flag = "No"

print("========== NUMBER ANALYZER ==========")
print()
print(f"Number: {number}")
print(f"Type: {type}")
print(f"Even/Odd: {status}")
print(f"Divisible by 5: {flag}")
print()
print("=====================================")


#DONE!!!!!!