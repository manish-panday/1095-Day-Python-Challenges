full_name = input("Enter your full name: ")
marks = int(input("Enter your mark (0-100): "))
grade = ""

if marks >= 90 and marks <=100:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B" 
elif marks >= 60:
    grade = "C" 
elif marks >= 50:
    grade = "D"
    
else:
    grade = "U"

print("========== STUDENT GRADE ==========")
print()
print(f"Student: {full_name}")
print(f"Marks: {marks}")
print(f"Grade: {grade}")
print()
print("====================================================")

#DONE !!!!!!!!!
