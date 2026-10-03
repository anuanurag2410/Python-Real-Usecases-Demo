# Databricks notebook source
print("Starting Class 3 for File Format and APIs")

# COMMAND ----------

#reading the data form dbfs the csv format 

df1 = spark.read.csv("dbfs:/FileStore/shared_uploads/anuanurag2410@gmail.com/global_food_wastage_dataset_2.csv",header=True,inferSchema=True)


# COMMAND ----------

df1.show()

# COMMAND ----------

display(df1)

# COMMAND ----------

df1.write.csv("dbfs:/FileStore/shared_uploads/anuanurag2410@gmail.com/output.csv",header=True,mode='overwrite')

# COMMAND ----------

df1.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC Reading from API

# COMMAND ----------

import requests

url = "https://real-time-amazon-data.p.rapidapi.com/product-details"

querystring = {"asin":"B07ZPKBL9V","country":"US"}

headers = {
	"x-rapidapi-key": "735d1841c7msh5908b4d65739c2ap1c43c0jsnff541268d977",
	"x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data=response.json()
print(json.dumps(data,indent=4))

# COMMAND ----------

import requests

url = "https://linkedin-job-search-api.p.rapidapi.com/active-jb-24h"

headers = {
	"x-rapidapi-key": "735d1841c7msh5908b4d65739c2ap1c43c0jsnff541268d977",
	"x-rapidapi-host": "linkedin-job-search-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

data=response.json()
print(json.dumps(data,indent=4))

# COMMAND ----------

import requests
import json 
import time 
import pandas as pd 
from pyspark.sql.types import StructType, StructField, StringType


for i in range(5):
    response=requests.get("https://api.spacexdata.com/v4/launches/latest")

    data=response.json()

    flatten_data={
        "name":data.get("name"),
        "date_utc":data.get("date_utc"),
        "rocket": data.get("rocket"),
        "success": str(data.get("success"))

    }

    print(json.dumps(flatten_data,indent=4))

    df=pd.DataFrame([flatten_data])

    sc = StructType([
    StructField("name", StringType(), True),
    StructField("date_utc", StringType(), True),
    StructField("rocket", StringType(), True),
    StructField("success", StringType(), True)
    ])


    df_spark=spark.createDataFrame(df,schema=sc)

    df_spark.write.mode("append").saveAsTable("spacex_launches1")

    display(df_spark)

    time.sleep(1)


# COMMAND ----------

# MAGIC %sql
# MAGIC select * from spacex_launches1

# COMMAND ----------

# MAGIC %sql
# MAGIC describe table spacex_launches1

# COMMAND ----------

# MAGIC %md
# MAGIC
