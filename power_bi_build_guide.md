# Optional Power BI Dashboard Build Guide

The included Streamlit dashboard is ready to run. This guide helps you recreate a Power BI version for interviews.

## 1. Load data
- Open Power BI Desktop → Get Data → Text/CSV → `data/retail_sales.csv`.
- Set `Order_Date` to Date, numeric fields to Decimal Number / Whole Number.
- Create a dedicated Date table and mark it as the Date table.

## 2. Suggested DAX measures
```DAX
Total Revenue = SUM(retail_sales[Revenue])

Total Profit = SUM(retail_sales[Profit])

Total Orders = DISTINCTCOUNT(retail_sales[Order_ID])

Units Sold = SUM(retail_sales[Quantity])

Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)

Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)
```

## 3. Recommended one-page layout
- Header: Retail Sales Performance | selected date range
- KPI cards: Total Revenue, Total Profit, Total Orders, Units Sold, Profit Margin %
- Row 2: Monthly Revenue & Profit line chart; Revenue by Category donut
- Row 3: Revenue by Region bar chart; Top 10 Products bar chart
- Row 4: Revenue by Channel; Revenue by Customer Segment
- Slicers: Order Date, Region, Category, Channel

## 4. Design guidance
Use a clean light background, navy title, restrained blue/teal accents, consistent currency formatting (₹), aligned visuals and readable labels. Avoid clutter and unnecessary 3D charts.

## 5. Interview explanation
Explain why each KPI matters, how slicers change the analysis, how you checked the revenue/profit calculations, and what business decision each visual could support.
