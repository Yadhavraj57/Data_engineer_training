import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="silver_patient",
    comment="Cleaned and transformed data (Silver Layer)"
)
def silver_patient():
    
    df = dlt.read("bronze_patient")

    df = df.withColumn("visit_date", to_date("visit_date"))

    df = df.withColumn("test_cost", df["tests_count"] * 500)

    df = df.withColumn("total_bill", df["test_cost"] + 1000)

    df = df.withColumn("visit_priority",
        when(df["visit_status"] == "Completed", 1)
        .when(df["visit_status"] == "Pending", 2)
        .otherwise(3)
    )

    # Remove invalid records
    df = df.filter(df["visit_status"].isNotNull())

    return df