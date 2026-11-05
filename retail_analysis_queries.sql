-- Retail Sales Analytics | SQL analysis queries
-- Load data/retail_sales.csv into a MySQL table named retail_sales.
-- Ensure Order_Date is DATE and Discount is DECIMAL (e.g. 0.10 = 10%).

-- 1. Overall KPI summary
SELECT COUNT(DISTINCT Order_ID) AS total_orders,
       SUM(Revenue) AS total_revenue,
       SUM(Profit) AS total_profit,
       SUM(Quantity) AS units_sold,
       ROUND(100 * SUM(Profit) / NULLIF(SUM(Revenue),0),2) AS profit_margin_pct
FROM retail_sales;

-- 2. Monthly revenue and profit trend
SELECT DATE_FORMAT(Order_Date,'%Y-%m') AS month,
       SUM(Revenue) AS revenue, SUM(Profit) AS profit
FROM retail_sales
GROUP BY DATE_FORMAT(Order_Date,'%Y-%m')
ORDER BY month;

-- 3. Category performance
SELECT Category, SUM(Revenue) AS revenue, SUM(Profit) AS profit,
       ROUND(100*SUM(Profit)/NULLIF(SUM(Revenue),0),2) AS margin_pct
FROM retail_sales
GROUP BY Category ORDER BY revenue DESC;

-- 4. Regional performance
SELECT Region, COUNT(DISTINCT Order_ID) AS orders,
       SUM(Revenue) AS revenue, SUM(Profit) AS profit
FROM retail_sales GROUP BY Region ORDER BY revenue DESC;

-- 5. Top 10 products
SELECT Product, SUM(Quantity) AS units_sold, SUM(Revenue) AS revenue
FROM retail_sales GROUP BY Product ORDER BY revenue DESC LIMIT 10;

-- 6. Channel contribution
SELECT Channel, SUM(Revenue) AS revenue,
       ROUND(100*SUM(Revenue)/(SELECT SUM(Revenue) FROM retail_sales),2) AS revenue_share_pct
FROM retail_sales GROUP BY Channel ORDER BY revenue DESC;

-- 7. High-discount orders (15% or more)
SELECT Order_ID, Order_Date, Product, Discount, Revenue, Profit
FROM retail_sales WHERE Discount >= 0.15 ORDER BY Discount DESC;

-- 8. Monthly category ranking using a window function
WITH monthly_category AS (
  SELECT DATE_FORMAT(Order_Date,'%Y-%m') AS month, Category,
         SUM(Revenue) AS revenue
  FROM retail_sales GROUP BY DATE_FORMAT(Order_Date,'%Y-%m'), Category
)
SELECT month, Category, revenue,
       DENSE_RANK() OVER (PARTITION BY month ORDER BY revenue DESC) AS category_rank
FROM monthly_category ORDER BY month, category_rank;

-- 9. Profitability check by product
SELECT Product, SUM(Revenue) AS revenue, SUM(Profit) AS profit,
       ROUND(100*SUM(Profit)/NULLIF(SUM(Revenue),0),2) AS margin_pct
FROM retail_sales GROUP BY Product ORDER BY margin_pct;
