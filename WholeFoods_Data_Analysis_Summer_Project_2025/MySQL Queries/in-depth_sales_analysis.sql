USE wholefoods_sales;

#Best-Selling Day Overall
SELECT
	date,
    SUM(total_sales) AS daily_revenue
FROM
	sales_june_2025
GROUP BY
	date
ORDER BY
	daily_revenue DESC
LIMIT 1;

#Average Daily Revenue By Department
SELECT 
    department,
    ROUND(SUM(total_sales) / COUNT(DISTINCT date), 2) AS avg_daily_revenue
FROM 
    sales_june_2025
GROUP BY 
    department
ORDER BY 
    avg_daily_revenue DESC;
    
#Weekend vs Weekday Revenue Comparison
SELECT 
    CASE 
        WHEN DAYOFWEEK(date) IN (1, 7) THEN 'Weekend'
        ELSE 'Weekday'
    END AS day_type,
    ROUND(SUM(total_sales), 2) AS total_revenue
FROM 
    sales_june_2025
GROUP BY 
    day_type;

#Products Sold Every Day
SELECT 
    product,
    COUNT(DISTINCT date) AS days_sold
FROM 
    sales_june_2025
GROUP BY 
    product
HAVING 
    days_sold = 30
ORDER BY 
    product;





