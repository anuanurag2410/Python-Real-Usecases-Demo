# Databricks notebook source
pip install tqdm faker  wordcloud pandas matplotlib

# COMMAND ----------

# MAGIC %md
# MAGIC # Python Functions (reusable mini-machines)

# COMMAND ----------

# MAGIC %md
# MAGIC ### (a) Hello helper

# COMMAND ----------

# This is a tiny machine called a "function"
# It says hello to any name we give it
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Anurag"))   # The machine works! It says hello.


# COMMAND ----------

# MAGIC %md
# MAGIC ### (b) Attendance calculator

# COMMAND ----------

# This machine calculates attendance in percent
def attendance(total_classes, attended):
    # We do (attended / total) * 100 to get percent
    percent = (attended / total_classes) * 100
    return round(percent, 2)  # Round to 2 digits like 75.55

print(attendance(150, 130))   # 72.0


# COMMAND ----------

# MAGIC %md
# MAGIC ### (c) Price after discount

# COMMAND ----------

# This machine tells us price after discount
def price_after_discount(price, discount_percent):
    # Take away a small part (discount) from price
    discount = price * (discount_percent / 100)
    return round(price - discount, 2)

print(price_after_discount(1000, 25))  # 750.0


# COMMAND ----------

# MAGIC %md
# MAGIC # 2) tqdm – progress bar for loops (looks cool!)

# COMMAND ----------

# MAGIC %md
# MAGIC ### (a) Simple progress

# COMMAND ----------

from tqdm import tqdm
import time

# We do 50 tiny tasks; tqdm shows a moving bar
for step in tqdm(range(50), desc="Doing tiny tasks"):
    time.sleep(0.1)  # pretend we are working slowly


# COMMAND ----------

# MAGIC %md
# MAGIC ### (b) Checking assignments

# COMMAND ----------

from tqdm import tqdm
import time

students = ["Anurag", "Stuti", "Sahil", "Neha", "Arjun"]
for name in tqdm(students, desc="Checking assignments"):
    time.sleep(0.2)  # checking takes time


# COMMAND ----------

# MAGIC %md
# MAGIC ### (c) Downloading files (pretend)

# COMMAND ----------

from tqdm import tqdm
import time

files = [f"file_{i}.pdf" for i in range(1, 11)]
for f in tqdm(files, desc="Downloading"):
    time.sleep(1)  # pretend download


# COMMAND ----------

# MAGIC %md
# MAGIC # 3) faker – make fake data quickly

# COMMAND ----------

# MAGIC %md
# MAGIC ### (a) Fake student records

# COMMAND ----------

from faker import Faker
import random

fake = Faker()
# Make 10 pretend students with name, roll, marks
for _ in range(20):
    name = fake.name()                        # Generate a fake student name
    roll = fake.random_int(min=1, max=100)    # Generate a random roll number between 1 and 100
    marks = random.randint(30, 100)           # Generate random marks between 30 and 100
    print(name, "| Roll:", roll, "| Marks:", marks)  # Print the fake student record


# COMMAND ----------

# MAGIC %md
# MAGIC ### (b) Fake canteen orders

# COMMAND ----------

from faker import Faker
import random

fake = Faker()
items = ["Samosa", "Maggie", "Sandwich", "Juice"]  # List of canteen items

# Generate 5 fake canteen orders
for _ in range(5):
    item = random.choice(items)         # Randomly pick an item
    qty  = random.randint(1, 5)         # Random quantity between 1 and 5
    time = fake.time()                  # Generate a fake order time
    print(time, "-", item, "x", qty)    # Print the fake order details


# COMMAND ----------

# MAGIC %md
# MAGIC ### (c) Fake emails list

# COMMAND ----------

from faker import Faker
fake = Faker()

emails = [fake.email() for _ in range(10)]
print(emails)  # pretend email list for a newsletter


# COMMAND ----------

# MAGIC %md
# MAGIC # 4 - Pandas – tiny data analysis

# COMMAND ----------

# MAGIC %md
# MAGIC ### (a) Who is topper? What’s the average?

# COMMAND ----------

import pandas as pd

data = {"Student": ["Anurag", "Stuti", "Sahil", "Neha", "Arjun"],
        "Marks":   [78,      92,      56,      88,      45]}
df = pd.DataFrame(data)

# Topper = biggest marks
topper_row = df.loc[df["Marks"].idxmax()]
print("Topper:", topper_row["Student"], "-", topper_row["Marks"])

# Average = middle value idea
print("Average Marks:", round(df["Marks"].mean(), 2))


# COMMAND ----------

# MAGIC %md
# MAGIC ### (b) Filter: only pass (>=40)

# COMMAND ----------

import pandas as pd

df = pd.DataFrame({"Student": ["Anurag", "Stuti", "Ankur", "Shikhar"], "Marks": [92, 60, 90, 25]})
passed = df[df["Marks"] >= 40]
display(passed)  # shows only students who passed


# COMMAND ----------

# MAGIC %md
# MAGIC ### (c) Group canteen sales by item

# COMMAND ----------

import pandas as pd

# Create a DataFrame with canteen sales data
df = pd.DataFrame({
    "Item": ["Samosa","Samosa","Juice","Sandwich","Juice","Samosa"],
    "Qty":  [2,        3,       1,      4,         2,       7]
})

# Group by item and sum the quantities sold for each item
totals = df.groupby("Item")["Qty"].sum().reset_index()

# Display the total quantity sold per item
display(totals)


# COMMAND ----------

# MAGIC %md
# MAGIC # 5- wordcloud – make pretty word pictures

# COMMAND ----------

# MAGIC %md
# MAGIC ### (a) Basic word cloud

# COMMAND ----------

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Input text for the word cloud
text = "Python Data AI Success Career Python Data AI"

# Generate a word cloud image from the text
wc = WordCloud(width=500, height=250, background_color="white").generate(text)

# Display the generated word cloud image
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")  # hide axes for a cleaner look
plt.show()


# COMMAND ----------

# MAGIC %md
# MAGIC ### (b) Word cloud from a list (join words)

# COMMAND ----------

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# List of words to include in the word cloud
words = ["SQL","Python","Spark","Cloud","ETL","SQL","Python","AI"]

# Join the list into a single string (required by WordCloud)
text = " ".join(words)  # make one big string

# Generate the word cloud image from the text
wc = WordCloud(width=500, height=250, background_color="white").generate(text)

# Display the generated word cloud image
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")  # hide axes for a cleaner look
plt.show()


# COMMAND ----------

# MAGIC %md
# MAGIC # 6- matplotlib – cute charts

# COMMAND ----------

# MAGIC %md
# MAGIC ### (a) Canteen sales bar chart

# COMMAND ----------

import matplotlib.pyplot as plt

# List of canteen items
items = ["Samosa", "Maggie", "Sandwich", "Juice"]
# Corresponding sales quantities for each item
sales = [120, 90, 60, 90]

plt.bar(items, sales)          # bars show how many sold
plt.title("Canteen Sales Today")  # chart title
plt.xlabel("Items")               # x-axis label
plt.ylabel("Quantity Sold")       # y-axis label
plt.show()                        # display the bar chart


# COMMAND ----------

# MAGIC %md
# MAGIC ### b)Time split (pie)

# COMMAND ----------

import matplotlib.pyplot as plt

# List of daily activities
activities = ["GYM", "Work", "Phone", "Sleep"]
# Corresponding hours spent on each activity
hours      = [1.5,       8,        2,       8]

# Create a pie chart to visualize time spent on each activity
plt.pie(hours, labels=activities, autopct="%1.0f%%")  # show % on slices
plt.title("My Day in a Pizza Pie")  # chart title
plt.show()  # display the pie chart


# COMMAND ----------


