@dlt.table
def silver_hospital():

    df = dlt.read("bronze_hospital")

    return df.withColumn(
        "total_bill",
        df.consultation_fee + (df.tests_count * 1000)
    )