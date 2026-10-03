# Databricks notebook source
# MAGIC %md
# MAGIC Apache Spark is a distributed engine that runs code across clusters, making it ideal for processing massive datasets efficiently.

# COMMAND ----------

print("Class 6 of Pyspakr ")

# COMMAND ----------

# MAGIC %md
# MAGIC ## PySpark vs Pandas

# COMMAND ----------

# MAGIC %md
# MAGIC Pandas is fast for small data, PySpark is scalable for distributed Big Data.

# COMMAND ----------

import pandas as pd 
pd_df=pd.DataFrame(data={'Column1': [1, 2, 3], 'Column2': ['a', 'b', 'c']})
spark_df=spark.createDataFrame(pd_df)
display(spark_df)


# COMMAND ----------

import pandas as pd
pd_df = pd.read_csv("global_food_wastage_dataset.csv")
display(pd_df)

# COMMAND ----------

df1 = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("dbfs:/FileStore/shared_uploads/anurag.srivastava@koantekorg.onmicrosoft.com/global_food_wastage_dataset.csv")
display(df1)

# COMMAND ----------

# MAGIC %md
# MAGIC # Creating & Exploring DataFrames

# COMMAND ----------

data = [("Alice", 25), ("Bob", 30)]
df=spark.createDataFrame(data, ["name", "age"])
df.printSchema()
display(df.describe())

# COMMAND ----------

# MAGIC %md
# MAGIC # Transformations vs Actions 

# COMMAND ----------

from pyspark.sql.functions import *

#transformation
df = df.withColumn("age_group", when(col("age") < 30, "Young").otherwise("Senior"))
df_filtered = df.filter(col("age") > 25)

#action 
display(df_filtered)

df.groupBy("age_group").count().show()

# COMMAND ----------

df.columns

# COMMAND ----------

df.dtypes

# COMMAND ----------

df.select("name").distinct().show()

# COMMAND ----------

#Column Funtions

df=df.withColumnRenamed("age", "customer_age")
df=df.withColumn("customer_age",col("customer_age").cast("int"))

# COMMAND ----------

display(df)

# COMMAND ----------

# DBTITLE 1,Filter and Logic
df.filter((col("customer_age") > 25) & (col("name") == "Alice")).show()

# COMMAND ----------

# DBTITLE 1,Nulls & Duplicates
df=df1.dropna()
df=df1.fillna({"Year": 0})
df=df1.dropDuplicates(["Year"])

# COMMAND ----------

display(df1)

# COMMAND ----------

# DBTITLE 1,Sorting
display(df1.orderBy(col("Year").desc()))

# COMMAND ----------

# DBTITLE 1,Aggregation
display(df1.groupBy("Year").count().orderBy(col("Year").desc()))

# COMMAND ----------

display(df1.groupBy("Country").agg(
    avg("Population (Million)").alias("avg_population"),
    max("Population (Million)").alias("max_populatin")
))

# COMMAND ----------

df1.columns

# COMMAND ----------

# MAGIC %md
# MAGIC # Date, Join & Window Functions

# COMMAND ----------

df = df.withColumn("order_date", to_date(col("order_date_str"), "yyyy-MM-dd"))
df = df.withColumn("year", year(col("order_date")))
df = df.withColumn("loaded_at", current_date())

# COMMAND ----------

df = df.withColumn("loaded_at", current_date())

# COMMAND ----------

display(df)

# COMMAND ----------

df1 = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])
df2 = spark.createDataFrame([(1, "New York"), (2, "Los Angeles")], ["id", "city"])

display(df1.join(df2, "id", "inner"))

# COMMAND ----------

df1.columns

# COMMAND ----------

from pyspark.sql.window import *
from pyspark.sql.functions import col, rank

windowSpec = Window.partitionBy("Year").orderBy(col("Year").desc())
df = df1.withColumn("rank", rank().over(windowSpec))
display(df)

# COMMAND ----------

df=df.repartition(4)
df=df.cache()


# COMMAND ----------

df.columns

# COMMAND ----------

import re

def clean_column_name(column_name):
    return re.sub(r'\W+', '', column_name)

cleaned_columns = [clean_column_name(col) for col in df.columns]
df = df.toDF(*cleaned_columns)

# COMMAND ----------

df = df.withColumnRenamed("aa", "Country").withColumnRenamed("aa", "Country")
df = df.withColumnRenamed("Food Category", "FoodCategory").withColumnRenamed("Food Category", "FoodCategory")
df = df.withColumnRenamed("Economic Loss", "EconomicLoss").withColumnRenamed("Economic Loss", "EconomicLoss")
df = df.withColumnRenamed("Avg Waste", "AvgWaste").withColumnRenamed("Avg Waste", "AvgWaste")
df = df.withColumnRenamed("Population (Million)", "Population").withColumnRenamed("Population (Million)", "Population")
df = df.withColumnRenamed("Household Waste (%)", "Household").withColumnRenamed("Household Waste (%)", "Household")
display(df)

# COMMAND ----------

df.columns

# COMMAND ----------

df.withColumnRenamed("Food Category", "Food_Category").write.mode("overwrite").saveAsTable("cache_tabe_final")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from cache_tabe_final 

# COMMAND ----------

# MAGIC %md
# MAGIC # Mini Project 

# COMMAND ----------

#Finding High Valued Customer
cust = spark.createDataFrame([(1,"Alice"),(2,"Bob")],["id","name"])
txn = spark.createDataFrame([(1, 500), (2, 200), (1, 400)], ["id", "amount"])

df=cust.join(txn, "id")
df=df.withColumn("High_Value_customer", when(col("amount")>300,"YES").otherwise("NO"))
display(df.groupBy("name").agg(sum("amount").alias("Total_Amount")))
df.write.mode("overwrite").saveAsTable("Customer_details")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from Customer_details 

# COMMAND ----------


