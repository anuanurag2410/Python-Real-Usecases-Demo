# Databricks notebook source
# MAGIC %sql
# MAGIC select * from default.spacex_launches limit 5 

# COMMAND ----------

df_sql= spark.sql("""
                  select name,rocket, success, date_utc from spacex_launches where success='True'
                  
                  """)

display(df_sql)

# COMMAND ----------

#loading the SQL Tables with PYSPARK

df_launches=spark.table("spacex_launches")
df_launches.printSchema()
display(df_launches)

# COMMAND ----------

#Filter only Success Missions

df_success=df_launches.filter(df_launches.success=='True')

display(df_success.select("rocket","success"))

# COMMAND ----------

#Group by on the Rocket 

df_grouped=df_success.groupBy("rocket").count().orderBy("count",ascending=False)
display(df_grouped)

# COMMAND ----------

#JOINS and AGGREGATION IN PYSPARK 

lookup_data = [
    ("Falcon 9", "A+"), ("Starship", "B"),
    ("Falcon Heavy", "A"), ("Dragon", "A"), ("Merlin", "C")
]
df_lookup = spark.createDataFrame(lookup_data, ["rocket", "rating"])

# COMMAND ----------

display(df_lookup)

# COMMAND ----------

display(df_success)

# COMMAND ----------

df_joined=df_success.join(df_lookup, on="rocket", how="left")
display(df_joined.select("name","rocket","rating","date_utc"))

# COMMAND ----------

from pyspark.sql.functions import count


df_rating_sumamry=df_joined.groupBy("rating").agg(count("name").alias("total_launches"))
display(df_rating_sumamry)

# COMMAND ----------

print(type(df_rating_sumamry))

# COMMAND ----------

df_pd=df_joined.toPandas()

# COMMAND ----------

print(type(df_pd))

# COMMAND ----------

df_pd["is_legacy"]=df_pd["date_utc"].apply(lambda x: int(x[:4]) <2022)
display(df_pd)

# COMMAND ----------

df_pd.to_csv("/Workspace/Shared/test.csv",index=False)

# COMMAND ----------

df_final=spark.createDataFrame(df_pd)
df_final.write.mode("overwrite").saveAsTable("spacex_python_sql_final_data")

# COMMAND ----------

df_final.createOrReplaceTempView("temp_view_spacex_data")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from spacex_python_sql_final_data

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC WITH recent_launches_cte AS (
# MAGIC   SELECT * FROM spacex_launches WHERE date_utc >= '2022-01-01'
# MAGIC ) 
# MAGIC
# MAGIC SELECT * FROM recent_launches_cte

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VIEW recent_launches_view AS
# MAGIC SELECT * FROM spacex_launches WHERE date_utc >= '2022-01-01';

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from recent_launches_view

# COMMAND ----------


