# PERSONAL POCKET CGPA CALCULATOR

print("====== PERSONAL POCKET CGPA CALCULATOR ======")

num_courses = int(input("Enter the number of courses: "))

total_units = 0
total_quality_points = 0

for i in range(num_courses):

    print(f"\nCourse {i+1}")

    course_code = input("Enter course code: ").upper()
    unit = int(input("Enter course unit: "))
    grade = input("Enter grade (A-F): ").upper()

    if grade == "A":
        point = 5

    elif grade == "B":
        point = 4

    elif grade == "C":
        point = 3

    elif grade == "D":
        point = 2

    elif grade == "E":
        point = 1

    elif grade == "F":
        point = 0

    else:
        print("Invalid grade!")
        continue

    quality_point = unit * point

    total_units += unit
    total_quality_points += quality_point

    print(f"{course_code}: {quality_point} Quality Points")

cgpa = total_quality_points / total_units

print("\n========== RESULT ==========")
print("Total Credit Units:", total_units)
print("Total Quality Points:", total_quality_points)
print("CGPA:", round(cgpa, 2))

if cgpa >= 4.50:
    print("Class of Degree: First Class")

elif cgpa >= 3.50:
    print("Class of Degree: Second Class Upper")

elif cgpa >= 2.40:
    print("Class of Degree: Second Class Lower")

elif cgpa >= 1.50:
    print("Class of Degree: Third Class")

else:
    print("Class of Degree: Pass")