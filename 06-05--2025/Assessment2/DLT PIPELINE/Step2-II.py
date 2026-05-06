import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="silver_orders",
    comment="Cleaned and transformed orders (Silver Layer)"
)
def silver_orders():

    df = dlt.read("bronze_orders")

    df = df.withColumn("order_date", to_date("order_date"))

    df = df.withColumn("total_order_value", df["quantity"] * 1000)

    df = df.withColumn("order_priority",
        when(df["order_status"] == "Delivered", 1)
        .when(df["order_status"] == "Pending", 2)
        .otherwise(3)
    )

    df = df.filter(df["order_status"].isNotNull())

    return df.select(
        "order_id",
        "product_id",
        "supplier_id",
        "order_date",
        "quantity",
        "order_status",
        "total_order_value",
        "order_priority"
    )