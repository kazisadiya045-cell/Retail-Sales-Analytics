# Retail Sales Analytics — End-to-End Data Analysis Project

## Project overview
An end-to-end retail analytics portfolio project built to demonstrate practical skills in **Python, Pandas, SQL, data visualization, KPI design and business communication**. The included Streamlit dashboard lets a recruiter or interviewer filter performance by date, region, category and sales channel.

> **Data transparency:** `data/retail_sales.csv` is a synthetic practice dataset generated for this portfolio project. It is not real company or customer data. Do not describe its findings as results from a real employer.

## Business problem
A retail business wants a single view of sales performance to answer:
1. How much revenue and profit are being generated?
2. Which months, regions, categories and products contribute most?
3. Which sales channels and customer segments drive revenue?
4. How do discounts relate to profitability?
5. Where should management investigate underperformance?

## Dataset
- 6,000 order-line records across 2023–2025
- Fields: Order_ID, Order_Date, Region, City, Category, Product, Channel, Customer_Segment, Quantity, Unit_Price, Discount, Revenue, Cost, Profit, Payment_Mode
- Revenue = Quantity × Unit_Price × (1 − Discount)
- Profit = Revenue − Cost
- Discount is stored as a decimal (0.10 means 10%).

## Tools
- Python 3.10+
- Pandas and NumPy for data preparation and analysis
- Plotly + Streamlit for the interactive dashboard
- MySQL 8+ for SQL analysis

## Run the dashboard
1. Install Python.
2. Extract the ZIP folder.
3. Open a terminal in this project folder.
4. Create and activate a virtual environment (recommended):
   - Windows: `py -m venv .venv` then `.venv\Scripts\activate`
5. Install packages: `pip install -r requirements.txt`
6. Start the app: `streamlit run app.py`
7. Browser opens the dashboard. If it does not, open the local URL printed in the terminal (usually `http://localhost:8501`).

## Project structure
```
Retail_Sales_Analytics_Project/
├── app.py
├── data/retail_sales.csv
├── sql/retail_analysis_queries.sql
├── reports/business_insights.md
├── reports/power_bi_build_guide.md
├── requirements.txt
└── README.md
```

## Analysis workflow
1. Define business questions and KPIs.
2. Inspect schema, data types, missing values and duplicates.
3. Validate calculations for revenue, cost and profit.
4. Create date fields and grouped summaries.
5. Analyze trends, category mix, regional contribution, channel and segment performance.
6. Build interactive dashboard and document recommendations.

## Suggested recruiter walkthrough (60–90 seconds)
“I built an end-to-end Retail Sales Analytics project using Python, SQL and an interactive dashboard. I prepared and validated a 6,000-row synthetic sales dataset, created business KPIs such as revenue, profit, order volume and profit margin, and analyzed trends across time, region, product category and channel. I used SQL aggregation and window functions for business questions, and Streamlit with Plotly to build a filterable dashboard. The goal was to turn transactional data into clear insights that could support inventory, pricing and sales decisions.”

## Important interview honesty
Call this a **self-initiated portfolio project using synthetic data**. Explain your own work and be ready to show the SQL queries, formulas, dashboard filters and validation steps. Do not claim the dataset represents actual company sales.
