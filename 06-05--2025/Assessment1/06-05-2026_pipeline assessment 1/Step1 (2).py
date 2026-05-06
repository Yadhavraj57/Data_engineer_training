import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="bronze_patient",
    comment="Raw patient visits data (Bronze Layer)"
)
def bronze_patient():
    
    data = [
        (1,1001,201,"2024-03-01","Completed",2),
        (2,1002,202,"2024-03-01","Completed",1),
        (3,1003,203,"2024-03-02","Completed",3),
        (4,1004,204,"2024-03-02","Pending",1),
        (5,1005,206,"2024-03-03","Completed",2)
    ]

    columns = ["visit_id","patient_id","doctor_id","visit_date","visit_status","tests_count"]

    df = spark.createDataFrame(data, columns)

    return df