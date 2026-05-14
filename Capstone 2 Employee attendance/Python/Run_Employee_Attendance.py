import os
print("Starting Employee Attendance Pipeline")
os.system("python employee_attendance_analysis.py")
os.system("python employee_attendance_pyspark.py")
print("Employee Attendance Pipeline Executed Successfully")