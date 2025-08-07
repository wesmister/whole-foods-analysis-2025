# whole-foods-analysis-2025
A data-analyst on accruate customer services sales using Python, SQL, and Power BI
# Whole Foods Sales Analysis (June 2025)

This project simulates a real-world end-to-end data analyst case study for Whole Foods Market. It includes data generation, SQL integration, and business intelligence visualizations built using Python, MySQL, and Power BI Fabric.

# Project Overview

This project analyzes simulated daily sales data for Whole Foods in June 2025. The workflow reflects a typical analytics pipeline — from raw data creation to database storage, querying, and interactive dashboard creation. It demonstrates skills in data engineering, SQL, analytics, and stakeholder communication.

---

# Tools & Technologies Used

- **Python (Pandas, MySQL Connector)**
- **MySQL Workbench & Server**
- **Power BI Fabric (Mac-compatible)**
- **Excel (for intermediate file handling)**

---

# Project Structure

WholeFoods_Sales_Analysis_2025:

'data/' —
Contains all data files used in the project
• 'WholeFoods_Sales_June2025.xlsx': Simulated Whole Foods daily sales data for June 2025
• 'products_sold_every_day.csv': Used for advanced product frequency analysis in Power BI
'python/' —
Scripts for data simulation and MySQL integration
• 'generate_sales_data.py': Python script to generate the sales dataset
• 'import_mysql.py': Python script to insert the dataset into MySQL
'sql/' —
SQL scripts for database setup and analysis
• 'create_database_and_table.sql': SQL statements to set up database and schema
• 'insert_script_notes.sql': Notes related to data insertion steps
• 'analysis_queries.sql': All SQL queries used to generate insights
'powerbi/' —
Dashboards and visuals
• 'WholeFoods_Basic_Dashboard.pdf': Initial dashboard with KPIs and simple visuals
• 'WholeFoods_Advanced_Insights.pdf': Second dashboard with in-depth analysis
• 'screenshots/': PNG exports of key visuals from Power BI
'daily_sales_trend.png'
'weekday_vs_weekend.png'
'kpi_cards.png'
'products_sold_every_day_table.png'

'README.md' —

        

---

# Key Business Insights

- Top 10 best-selling products by revenue
- Daily revenue trends across the month
- Department-level sales analysis
- Weekday vs. weekend sales behavior
- Products sold consistently every day
- KPIs including total revenue and average daily sales

---

# How to Use

1. **Data Simulation:** Run `generate_sales_data.py` to create the dataset.
2. **Database Insertion:** Use `import_mysql.py` to load data into MySQL.
3. **Run SQL Queries:** Refer to `all_queries.sql` to extract insights.
4. **Visualize:** Open the PDF dashboards under `/PowerBI` to view visual summaries.

---

# Future Extensions

- Add forecasting and regression using Python (e.g., `statsmodels`, `sklearn`)
- Include region or store-specific analysis
- Automate data pipeline using Python scripts
- Deploy interactive dashboards online
