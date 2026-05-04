import dlt
from pyspark.sql.functions import *
@dlt.table
def bronze_hospital():

    data = [
    (101,"Arjun Reddy","Hyderabad","Cardiology",5000,1),
    (102,"Sneha Kapoor","Delhi","Orthopedics",3000,2),
    (103,"Rahul Sharma","Mumbai","Dermatology",1500,1)
    ]

    columns = [
    "visit_id",
    "patient_name",
    "city",
    "department",
    "consultation_fee",
    "tests_count"
    ]

    return spark.createDataFrame(data, columns)