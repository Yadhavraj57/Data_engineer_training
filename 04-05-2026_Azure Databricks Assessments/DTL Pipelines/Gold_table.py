from pyspark.sql.functions import sum
@dlt.table
def gold_hospital():
    df = dlt.read("silver_hospital")
    return df.groupBy("department").agg(sum("total_bill").alias("total_revenue"))