# Databricks notebook source
# MAGIC %sql 
# MAGIC select 1 

# COMMAND ----------

print("This is my First Python Class")

# COMMAND ----------

# MAGIC %md
# MAGIC Python Variable

# COMMAND ----------

product_name='laptop'
price=5999.99
in_stock=True
print("Price before reassigning: ",price)

price= "ANURAG"


print("Product: ",product_name)
print("Price: ",price)
print("Avaliable :",in_stock)

# COMMAND ----------

# MAGIC %md
# MAGIC # **Python Operators and Expressions**

# COMMAND ----------

total_sales=5000
discount=10

final_amount=total_sales- (total_sales*(discount/100))
print(f"Final Amount After {discount}% Discount : {final_amount}")


# COMMAND ----------

0.1+0.2 == 0.3

# COMMAND ----------

import math 

math.isclose(0.1+0.2,0.3)

# COMMAND ----------

product_price=10

# COMMAND ----------

def calculate_tax(price):
    tax=price*0.18    #Applying 18% GST
    return tax


product_price=5000
tax_amount=calculate_tax(product_price)
print(f"Tax on {product_price} is {calculate_tax(product_price)}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## **REPL Execution Model**
# MAGIC
# MAGIC
# MAGIC ### 1️⃣ **Read** - Reads user input
# MAGIC ### 
# MAGIC ### 2️⃣ **Evaluate** - Processes the code
# MAGIC ### 
# MAGIC ### 3️⃣ **Print** - Displays the output
# MAGIC ### 
# MAGIC ### 4️⃣ **Loop** - Repeats the process

# COMMAND ----------

x=10
y=6

z=x//y
print(z)

# COMMAND ----------


