import mysql.connector
import pandas as pd

#Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lebron4life!",
    database="wholefoods_sales"
)

cursor= conn.cursor ()
print("Connected to MySQL!")

#Read Excel File
df = pd.read_excel("WholeFoods_Sales_June2025.xlsx")

#Insert each row into MySQL
for _, row in df.iterrows ():
    cursor.execute ("""
        INSERT INTO sales_june_2025 (date, department, product, unit_price, units_sold, total_sales)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        row['Date'],
        row['Department'],
        row['Product'],
        row['Unit Price ($)'],
        row['Units Sold'],
        row['Total Sales ($)']
    ))
#Commit the transaction
conn.commit()
print ("Data inserted into MySQL!")

cursor.close()
conn.close()

