# Databricks notebook source
import pandas as pd

# COMMAND ----------

df=pd.read_csv("./mcdonalds_dummy_menu_1000.csv")
display(df)

# COMMAND ----------

print(df.isnull().sum())

# COMMAND ----------

print(df.dtypes)

# COMMAND ----------

df["description"]=df["description"].fillna("No description")
df["is_available"]=df["is_available"].astype(int)

# COMMAND ----------

display(df)

# COMMAND ----------

df_spark=spark.createDataFrame(df)
display(df_spark)

# COMMAND ----------

df_spark.printSchema()

# COMMAND ----------

from pyspark.sql.functions import *

#Feature Engineering to create Calories_Label
df_spark=df_spark.withColumn("Calories_Label",when(col('calories')>500,"High").otherwise("Normal"))


#Feature Engineering to create Price_Label
df_spark = df_spark.withColumn("price_category", when(col("price") > 6, "Premium")
                                .when(col("price") > 3, "Standard")
                                .otherwise("Budget"))

# COMMAND ----------

display(df_spark)


# COMMAND ----------

display(df_spark.select("name","calories","Calories_Label","price","price_category"))

# COMMAND ----------

# Average calories per category
df_grouped=df_spark.groupBy("category").avg("calories", "fat", "carbs").orderBy("avg(calories)", ascending=False)
display(df_grouped)


# Count of items per price category
df_price=df_spark.groupBy("price_category").count()
display(df_price)

# COMMAND ----------

df_spark.write.format("delta").mode("overwrite").saveAsTable("mcd_final_menu")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from mcd_final_menu 

# COMMAND ----------


