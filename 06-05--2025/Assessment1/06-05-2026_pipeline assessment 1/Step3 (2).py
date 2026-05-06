import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="gold_city",
    comment="Aggregated revenue by patient (Gold Layer)"
)
def gold_city_revenue():
    
    df = dlt.read("silver_patient")

    return df.groupBy("patient_id") \
             .agg(sum("total_bill").alias("total_revenue"))

@dlt.table(
    name="gold_specialization_revenue",
    comment="Aggregated revenue by doctor (Gold Layer)"
)
def gold_specialization_revenue():
    
    df = dlt.read("silver_patient_visits")

    return df.groupBy("city") \
         .agg(sum("total_bill").alias("total_revenue"))