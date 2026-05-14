import pandas as pd
import numpy as np

data = {
    "employee_id":[101,102,103,104],
    "employee_name":["Amit","Priya","Rahul","Sneha"],
    "department":["IT","HR","Finance","IT"],
    "clock_in":["09:00","09:30","10:00",None],
    "clock_out":["18:00","17:30","15:00","18:00"],
    "tasks_completed":[8,5,2,7]
}
df = pd.DataFrame(data)
print("Original Data")
print(df)
df["clock_in"] = df["clock_in"].fillna("09:00")
df["clock_in"] = pd.to_datetime(df["clock_in"])
df["clock_out"] = pd.to_datetime(df["clock_out"])
df["work_hours"] = (df["clock_out"] - df["clock_in"]).dt.total_seconds() / 3600
df["productivity_score"] = (df["tasks_completed"] / df["work_hours"])
df["attendance_status"] = np.where(df["work_hours"] < 6,"Frequent Absentee","Regular")
print("\nProcessed Data")
print(df)
top_performers = df.sort_values(by="productivity_score",ascending=False)
print("\nTop Performers")
print(top_performers)

summary = df.groupby("department")[["work_hours","productivity_score"]].mean()
print("\nDepartment Summary")
print(summary)