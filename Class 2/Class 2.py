# Databricks notebook source
c=3
print(f"Starting of Class {c}")

# COMMAND ----------

orders=["order_1","order_2","order_3","order_4"]
#for Loop Usecase 

for item in orders: 
    print(f"Processing your {item}✅")

# COMMAND ----------

for  num in range(1,20,2):
    #range(start,end,step)
    print(f"Processing your order_{num}✅")

# COMMAND ----------

#While Loop 

counter=10

while counter>=0:
    print(f"Bomb Will Blast in {counter} seconds....")
    # counter-=1 #decrementing. counter=counter-1
    counter=counter-1
print("Blasted🔥")

# COMMAND ----------

#Automate Password attempts in application

max_attempt=3
attempt=0
password="anurag123"

while attempt< max_attempt:
    user_input=input("Enter the Password : ")

    if user_input==password:
        print("Access Granted✅")
        break

    else:
        print("Incorrect Password, Try Again !!!!")
        attempt=attempt+1

# COMMAND ----------

#For Each Loop Example 
#list of Orders 
orders = [
    {"order_id": 101, "item": "Laptop", "price": 75000},
    {"order_id": 102, "item": "Phone", "price": 45000},
    {"order_id": 103, "item": "Tablet", "price": 20000}
]

for order in orders: 
    print(f"Processing Order #{order['order_id']}")



# COMMAND ----------

user_info = {
    "name": "Anurag Srivastava",
    "role": "Data Engineer",
    "experience": "4 years",
    "location": "Bangalore"
}

# For-Each Loop to iterate over dictionary items
for key, value in user_info.items():
    print(f"{key}: {value}")


# COMMAND ----------

#Functions 

def greet(name):
    print(f"Welcome to the Python Bootcamp {name}😍")

name=input("Enter the Name")
greet(name)

# COMMAND ----------

#calculate Discount on Ecommerce Store 

def discount_calculator(price,discount_rate):
    final_price=price-(price*discount_rate/100)
    return final_price

print(f"The final amount after discount is {discount_calculator(10000,10)}")


# COMMAND ----------

#lambda Funciton 
square=lambda x:x*x
print(f" THis is the Square lambda function {square(4)}")


# COMMAND ----------

#Sorting the Product Price 
products=[("Laptop",750000),("Phone",450000),("Tablet",56000)]

sorted_products=sorted(products, key=lambda x:x[1],reverse=True)
print(sorted_products)

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Exception handling**

# COMMAND ----------

x=2
counter=3
while counter>0:
  y=10/x
  x=x-1
  print(f"Value of Y is {y}")
  counter-=1

# COMMAND ----------

x=2
counter=5
while counter>0:
    try:
        y=10/x
    except:
        print("Cannot divide a number by Zero0️⃣")
        break
    x=x-1
    print(f"Value of Y is {y}")
    counter-=1

# COMMAND ----------

#Finally
try:
    file = open("data.txt", "r")
    data = file.read()
    result = int(data) / 0  # Raises ZeroDivisionError
except (FileNotFoundError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")

finally:
    file.close()  # Ensures file is closed
    print("File closed safely.")

# COMMAND ----------

#Else in Exception handling 

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    print(f"Computation successful! Result: {result}")
finally:
    print("Execution completed.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Interview Level Questions **Tricky Part**

# COMMAND ----------

1️⃣ What is the difference between for and while loops?
✅ Answer:

for loops iterate over a sequence (list, tuple, range).
while loops run as long as a condition is True.

# COMMAND ----------

2️⃣ What is the difference between return and print in functions?
✅ Answer:

return sends the result back to the caller.
print just displays the result but doesn’t return it.

# COMMAND ----------

3️⃣ What is the difference between try-except and try-except-finally?
✅ Answer:

try-except catches errors and prevents crashes.
finally executes no matter what (used for cleanup like closing files).

