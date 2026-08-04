full_name = input("Enter your full name:")
math_mark = int(input("Enter your math marks:"))
science_mark = int(input('Enter your science mark: '))
english_mark = int(input("Enter your english mark: "))

total_mark = int((math_mark + science_mark + english_mark))
average_mark = int((total_mark)/ 3)

print("========== STUDENT REPORT ==========")
print()
print(f"Student: {full_name}")
print()
print(f"Mathematics: {math_mark}")
print(f"Science: {science_mark}")
print(f"English: {english_mark}")
print()
print(f"Total Marks: {total_mark}")
print(f"Average Marks: {average_mark}")
print()
print("===================================")

#Done !!!!