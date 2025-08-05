CREATE DATABASE wholefoods_sales;
USE wholefoods_sales;
CREATE TABLE sales_june_2025 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    department VARCHAR(50),
    product VARCHAR(100),
    unit_price DECIMAL(5,2),
    units_sold INT,
    total_sales DECIMAL(7,2)
);

USE wholefoods_sales;
SELECT * FROM sales_june_2025 LIMIT 10;

#Total Sales by Department
SELECT department, SUM(total_sales) AS total_department_sales
FROM sales_june_2025
GROUP BY department
ORDER BY total_department_sales DESC;

#Top 10 Sales by Revenue
SELECT product, SUM(total_sales) AS total_product_sales
FROM sales_june_2025
GROUP BY product
ORDER BY total_product_sales DESC
LIMIT 10;

#Daily Sales Trend
SELECT date, SUM(total_sales) AS daily_sales
FROM sales_june_2025
GROUP BY date
ORDER BY date;

#Best-Selling Products in Each Department
SELECT department, product, SUM(total_sales) AS product_sales
FROM sales_june_2025
GROUP BY department, product
ORDER BY department, product_sales DESC;

#Average Units Sold per Product
SELECT product, AVG(units_sold) AS avg_units_sold
FROM sales_june_2025
GROUP BY product
ORDER BY avg_units_sold DESC
LIMIT 10;
