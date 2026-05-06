import dlt
from pyspark.sql.functions import *
@dlt.table(
    name="gold_city_revenue",
    comment="Revenue by supplier (Gold Layer)"
)
def gold_city_revenue():

    df = dlt.read("silver_orders")

    return df.groupBy("supplier_id") \
             .agg(sum("total_order_value").alias("total_revenue"))
@dlt.table(
    name="gold_category_revenue",
    comment="Revenue by product (Gold Layer)"
)
def gold_category_revenue():

    df = dlt.read("silver_orders")

    return df.groupBy("product_id") \
             .agg(sum("total_order_value").alias("total_revenue"))