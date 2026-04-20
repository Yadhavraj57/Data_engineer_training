import json
import csv
with open("students.txt", "r") as f:
    students = [line.strip() for line in f]
with open("marks.json", "r") as f:
    marks_data = json.load(f)
marks_dict = {}
for item in marks_data["students"]:
    marks_dict[item["name"]] = item["marks"]
attendance_dict = {}
with open("attendance.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["name"]
        present = int(row["days_present"])
        total = int(row["total_days"])
        attendance_percent = (present / total) * 100
        attendance_dict[name] = attendance_percent
for student in students:
    marks = marks_dict.get(student, 0)
    attendance = attendance_dict.get(student, 0)
    if marks >= 85:
        grade = "Excellent"
    elif marks >= 70:
        grade = "Good"
    else:
        grade = "Needs Improvement"

    print(f"Name: {student}")
    print(f"Marks: {marks}")
    print(f"Attendance: {attendance:.2f}%")
    print(f"Performance: {grade}")
    