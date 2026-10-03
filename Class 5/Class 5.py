# Databricks notebook source
# MAGIC %md
# MAGIC ##  Data Manipulation with Pandas in Databricks

# COMMAND ----------

# MAGIC %md
# MAGIC What is Pandas? 
# MAGIC
# MAGIC Pandas is a Python library for structured data manipulation — like Excel tables, but with code.

# COMMAND ----------

import pandas as pd

# Sample Pandas Series
sample_series = pd.Series([1, 2, 3, 4, 5], name="Sample Series")

# Sample Pandas DataFrame
sample_dataframe = pd.DataFrame({
    "Column1": [1, 2, 3, 4, 5],
    "Column2": ["A", "B", "C", "D", "E"]
})

display(sample_series)
display(sample_dataframe)

# COMMAND ----------

import pandas as pd 
import numpy as np

# COMMAND ----------

# MAGIC %md
# MAGIC ## Why We Use Pandas in the Data Domain
# MAGIC
# MAGIC 1-Clean the raw data .csv/API Data
# MAGIC 2- Analyse Transaction 
# MAGIC 3- Feature Engineering for ML
# MAGIC 4- Save the reports/export to BI

# COMMAND ----------

# MAGIC %md
# MAGIC **Q:** Why is Pandas preferred during data cleaning?
# MAGIC
# MAGIC **A:** It allows step-by-step data cleaning in memory, is fast, and integrates well with Databricks, making it perfect for pre-SQL transformation.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Filtering, Sorting, Aggregation

# COMMAND ----------

data = {
    'customer_id': [101, 102, 103, 104, 105, 106, 106],
    'age': [25, 30, np.nan, 45, 22, 40, 40],
    'purchase_amount': [200, 450, 300, np.nan, 150, 500, 500],
    'region': ['North', 'South', 'East', 'East', 'West', 'South', 'South']
}
df=pd.DataFrame(data)
display(df)


# COMMAND ----------

#filtering the South Customers 

display(df[df['region']=='South'])

# COMMAND ----------

display(df[df['region'].isin(['South', 'East'])])

# COMMAND ----------

#sort the high spenders on top

display(df.sort_values(by='purchase_amount',ascending=False))

# COMMAND ----------

#GROUP BY AND AGGREGATION
#Get region-wise average purchase amount
df.groupby('region')['purchase_amount'].mean()

# COMMAND ----------

# MAGIC %md
# MAGIC groupby()  ---> used to do row_level Grouping.
# MAGIC
# MAGIC
# MAGIC
# MAGIC pivot_table() ---> is for cross-tabulation and summarizing mutiple fields in 2D

# COMMAND ----------

import pandas as pd

# Sample data
data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'age': [25, 34, 45, 23, 35, 40],
    'purchase_amount': [100, 200, 150, 300, 250, 50],
    'region': ['North', 'South', 'East', 'West', 'North', 'South'],
    'product': ['A', 'B', 'A', 'B', 'A', 'B']
}

# Create DataFrame
df_pivot = pd.DataFrame(data)

# Demonstrate pivot_table
pivot_table = pd.pivot_table(df_pivot, values='purchase_amount', index='region', columns='product', aggfunc='mean')

display(pivot_table)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Handling Missing Values, Duplicates, Outliers 

# COMMAND ----------

display(df)

# COMMAND ----------

#check the nulls 
df.isnull().sum()



# COMMAND ----------

#Fill the Missing Values
df['age']=df['age'].fillna(df['age'].mean())
display(df)

# COMMAND ----------

#Remove the missing Purcahce row 
df=df.dropna(subset=['purchase_amount'])
display(df)


# COMMAND ----------

# MAGIC %md
# MAGIC what is OUTLIER?
# MAGIC
# MAGIC An outlier is a data point that is significantly different from the rest of the data.
# MAGIC
# MAGIC It lies far away from other values and can affect averages, predictions, and model accuracy if not handled properly.
# MAGIC
# MAGIC example =[1,2,3,4,100]

# COMMAND ----------

# MAGIC %md
# MAGIC ## Outlier Detection
# MAGIC ## 
# MAGIC ## We use IQR Method to dedect the data in the OUtliers 
# MAGIC
# MAGIC **IQR = Interquartile Range = Q3 - Q1
# MAGIC
# MAGIC Q1 (25th percentile) → 25% of the data lies below this value
# MAGIC
# MAGIC Q3 (75th percentile) → 75% of the data lies below this value
# MAGIC
# MAGIC IQR measures the spread of the middle 50% of the data**
# MAGIC
# MAGIC
# MAGIC inbuild fucntion for percentile --> quantile(0.25)
# MAGIC this will give me 25% percentile
# MAGIC
# MAGIC
# MAGIC LOGIC 
# MAGIC A data point is an outlier if:
# MAGIC
# MAGIC Below: value < Q1 - 1.5 * IQR
# MAGIC
# MAGIC Above: value > Q3 + 1.5 * IQR
# MAGIC

# COMMAND ----------

import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(42)
data = {
    'customer_id': range(1, 101),
    'age': np.random.randint(18, 70, size=100),
    'purchase_amount': np.concatenate([np.random.normal(50, 10, 95), np.random.normal(200, 10, 5)]),
    'region': np.random.choice(['North', 'South', 'East', 'West'], size=100)
}

# Create DataFrame
df = pd.DataFrame(data)

# Introduce some missing values
df.loc[5:10, 'age'] = np.nan
df.loc[15:20, 'purchase_amount'] = np.nan

display(df)

# COMMAND ----------

#Applying IQR method
# Below: value < Q1 - 1.5 * IQR
# Above: value > Q3 + 1.5 * IQR

Q1=df['purchase_amount'].quantile(0.25)
Q3=df['purchase_amount'].quantile(0.75)

IQR=Q3-Q1

outliers=df[(df['purchase_amount']<Q1-1.5*IQR) | (df['purchase_amount']>Q3+1.5*IQR)]
display(outliers)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Feature Engineering and Data Transfomation

# COMMAND ----------

# MAGIC %md
# MAGIC Feature Engineering is the process of creating, modifying, or selecting features (columns) from raw data to improve the performance of machine learning models.
# MAGIC
# MAGIC You’re basically preparing your data to make it more meaningful and useful for the model.

# COMMAND ----------

b=[18,35,50,70]
labels=['young','young adult','adult']

df['age_group']=pd.cut(df['age'],bins=bins,labels=labels)
display(df)

# COMMAND ----------

#High-Valued Customer

df['high_value_customer'] = df['purchase_amount'].apply(lambda x : 'yes' if x > 200 else 'no')
display(df)

# COMMAND ----------

#Tag a Customer 

df['customer_tag'] = df['region'] + '_' + df['age_group'].astype(str)
display(df)

# COMMAND ----------

#Save the Data to CSV for some BI Reports

df.to_csv('/Workspace/Users/anurag.srivastava@koantekorg.onmicrosoft.com/Python Bootcamp/reporting_new.csv', index=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ### ✅ Q1: How do you verify your cleaning logic?
# MAGIC
# MAGIC **Answer:**
# MAGIC
# MAGIC - Compare row count before/after
# MAGIC - Use `.describe()` to check for value range changes
# MAGIC - Validate nulls with `.isnull().sum()`
# MAGIC - Cross-check business constraints (e.g., no age > 100)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Q2: What if your `drop_duplicates()` removes valid business data?
# MAGIC
# MAGIC **Answer:**
# MAGIC Use `drop_duplicates(subset=['customer_id', 'region'])`
# MAGIC
# MAGIC or create a **unique key** using `customer_id + timestamp` to safely deduplicate.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Q3: Where does Pandas fit in ETL pipeline?
# MAGIC
# MAGIC **Answer:**
# MAGIC Pandas fits into the **Transform** phase (T in ETL). It's best for:
# MAGIC
# MAGIC - Rapid cleanup before ingestion
# MAGIC - Logic testing before Spark pipelines
# MAGIC - Quick validation before loading to DB
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Q4: How do you handle outliers practically?
# MAGIC
# MAGIC **Answer:**
# MAGIC
# MAGIC - Detect using IQR or Z-score
# MAGIC - Instead of dropping, **cap to 95th percentile** or **flag with a binary column**
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### ✅ Q5: Why avoid `index=True` in `to_csv()`?
# MAGIC
# MAGIC **Answer:**
# MAGIC Because index adds an unwanted column (`0, 1, 2…`) which doesn’t carry meaning and messes up SQL reads.
