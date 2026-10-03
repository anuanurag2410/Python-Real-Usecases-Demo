# Databricks notebook source
print("Welcome to Class 7 ")

# COMMAND ----------

import requests
import pandas as pd

# Post IDs you want to analyze
post_ids = ["3142351097879579233", "17896441985824751"]

# RapidAPI Auth
headers = {
    "x-rapidapi-key": "735d1841c7msh5908b4d65739c2ap1c43c0jsnff541268d977",
    "x-rapidapi-host": "instagram230.p.rapidapi.com"
}



# COMMAND ----------

#Normalising the JSON

comments_lists=[]

for pk in post_ids:
    url="https://instagram230.p.rapidapi.com/post/comments"
    querystring={"pk":pk}

    response=requests.get(url, headers=headers, params=querystring)
    data=response.json()

    for comment in data.get("comments",[]):
        user=comment.get("user",{})
        comments_lists.append({
            "post_id":pk,
            "username":user.get("username",""),
            "full_name":user.get("full_name",""),
            "is_verified":user.get("is_verified"),
            "is_private":user.get("is_private"),
            "comment_text":comment.get("text",""),
            "likes":comment.get("comment_like_count"),
            "created_at":pd.to_datetime(comment.get("created_at"),unit="s")
        })
        



# COMMAND ----------

comments_lists

# COMMAND ----------

df=pd.DataFrame(comments_lists)
display(df)

# COMMAND ----------

from pyspark.sql.types import * 

schema = StructType([
    StructField("post_id", StringType(), True),
    StructField("username", StringType(), True),
    StructField("full_name", StringType(), True),
    StructField("is_verified", BooleanType(), True),
    StructField("is_private", BooleanType(), True),
    StructField("comment_text", StringType(), True),
    StructField("likes", IntegerType(), True),
    StructField("created_at", TimestampType(), True)
])

df_spark = spark.createDataFrame(df, schema)
display(df_spark)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Filtering and Cleaning

# COMMAND ----------

df_filtered=df_spark.filter(df_spark.comment_text.isNotNull())
display(df_filtered)

# COMMAND ----------

df_filtered.write.mode("append").saveAsTable("Instagram_cleaned_comments")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from Instagram_cleaned_comments 

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history Instagram_cleaned_comments 

# COMMAND ----------


