# whole-foods-analysis-2025
A full-stack data analyst project using Python, SQL, and Power BI
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

WholeFoods_Sales_Analysis_2025/
│
├── Python/
│ └── generate_sales_data.py # Creates the simulated dataset
│ └── import_mysql.py # Inserts data into MySQL
│
├── SQL/
│ └── all_queries.sql # SQL queries for analysis
│
├── PowerBI/
│ └── simple_dashboard.pdf # Basic Power BI dashboard
│ └── advanced_dashboard.pdf # Deep-dive Power BI dashboard
│
├── Data/
│ └── WholeFoods_Sales_June2025.xlsx # Final dataset used
│
├── Docs/
│ └── WholeFoods_Project_Summary.pdf # Detailed project summary


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
- Include region- or store-specific analysis
- Automate data pipeline using Python scripts
- Deploy interactive dashboards online

---

# Screenshots

![Simple Dashboard](PowerBI/simple_dashboard.png)
![Advanced Dashboard](PowerBI/advanced_dashboard.png)
