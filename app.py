import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Retail Sales Intelligence", page_icon="📊", layout="wide")
st.markdown("""
<style>
.main {background:#f5f7fb;}
.block-container {padding-top:1.4rem; padding-bottom:2rem;}
[data-testid="stMetric"] {background:white; padding:18px 18px 14px; border:1px solid #e7ebf3; border-radius:12px;}
h1,h2,h3 {color:#15233b;}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    p=Path(__file__).parent/"data"/"retail_sales.csv"
    d=pd.read_csv(p,parse_dates=["Order_Date"])
    d["Month"]=d["Order_Date"].dt.to_period("M").astype(str)
    d["Year"]=d["Order_Date"].dt.year.astype(str)
    d["Profit_Margin"]=d["Profit"]/d["Revenue"].replace(0, pd.NA)
    return d

df=load_data()
st.title("Retail Sales Intelligence Dashboard")
st.caption("Executive view | Sales performance • Profitability • Product mix • Regional trends")
with st.sidebar:
    st.header("Dashboard filters")
    min_date,max_date=df.Order_Date.min().date(),df.Order_Date.max().date()
    date_range=st.date_input("Order date range", value=(min_date,max_date), min_value=min_date,max_value=max_date)
    regions=st.multiselect("Region",sorted(df.Region.unique()),default=sorted(df.Region.unique()))
    categories=st.multiselect("Category",sorted(df.Category.unique()),default=sorted(df.Category.unique()))
    channels=st.multiselect("Sales channel",sorted(df.Channel.unique()),default=sorted(df.Channel.unique()))

if isinstance(date_range,tuple) and len(date_range)==2:
    start,end=date_range
else:
    start,end=min_date,max_date
f=df[(df.Order_Date.dt.date>=start)&(df.Order_Date.dt.date<=end)&df.Region.isin(regions)&df.Category.isin(categories)&df.Channel.isin(channels)]
if f.empty:
    st.warning("No records match these filters. Please widen your selection.")
    st.stop()

sales=f.Revenue.sum()
profit=f.Profit.sum()
orders=f.Order_ID.nunique()
units=f.Quantity.sum()
margin=(profit/sales*100) if sales else 0
a,b,c,d,e=st.columns(5)
a.metric("Total revenue",f"₹{sales:,.0f}")
b.metric("Total profit",f"₹{profit:,.0f}")
c.metric("Orders",f"{orders:,}")
d.metric("Units sold",f"{units:,}")
e.metric("Profit margin",f"{margin:.1f}%")
st.divider()

left,right=st.columns([1.65,1])
with left:
    st.subheader("Monthly revenue trend")
    monthly=f.groupby("Month",as_index=False).agg(Revenue=("Revenue","sum"),Profit=("Profit","sum"))
    fig=px.line(monthly,x="Month",y=["Revenue","Profit"],markers=True,template="plotly_white",
                color_discrete_sequence=["#3157a4","#17a589"])
    fig.update_layout(legend_title_text="", xaxis_title="", yaxis_title="Amount (₹)", margin=dict(l=10,r=10,t=20,b=10))
    st.plotly_chart(fig,use_container_width=True)
with right:
    st.subheader("Revenue by category")
    cat=f.groupby("Category",as_index=False).Revenue.sum().sort_values("Revenue",ascending=False)
    fig=px.pie(cat,names="Category",values="Revenue",hole=.58,template="plotly_white",
               color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(legend_title_text="",margin=dict(l=5,r=5,t=20,b=5))
    st.plotly_chart(fig,use_container_width=True)

left,right=st.columns(2)
with left:
    st.subheader("Regional performance")
    reg=f.groupby("Region",as_index=False).agg(Revenue=("Revenue","sum"),Profit=("Profit","sum"))
    fig=px.bar(reg,x="Region",y="Revenue",color="Profit",color_continuous_scale="Blues",template="plotly_white")
    fig.update_layout(xaxis_title="",yaxis_title="Revenue (₹)",margin=dict(l=5,r=5,t=15,b=5))
    st.plotly_chart(fig,use_container_width=True)
with right:
    st.subheader("Top 10 products by revenue")
    top=f.groupby("Product",as_index=False).agg(Revenue=("Revenue","sum"),Units=("Quantity","sum")).nlargest(10,"Revenue").sort_values("Revenue")
    fig=px.bar(top,x="Revenue",y="Product",orientation="h",text_auto=",.0f",template="plotly_white",
               color="Revenue",color_continuous_scale="Teal")
    fig.update_layout(xaxis_title="Revenue (₹)",yaxis_title="",coloraxis_showscale=False,margin=dict(l=5,r=5,t=15,b=5))
    st.plotly_chart(fig,use_container_width=True)

st.subheader("Channel and customer segment")
x,y=st.columns(2)
with x:
    ch=f.groupby("Channel",as_index=False).Revenue.sum()
    st.plotly_chart(px.bar(ch,x="Channel",y="Revenue",color="Channel",template="plotly_white"),use_container_width=True)
with y:
    seg=f.groupby("Customer_Segment",as_index=False).Revenue.sum()
    st.plotly_chart(px.bar(seg,x="Customer_Segment",y="Revenue",color="Customer_Segment",template="plotly_white"),use_container_width=True)

st.subheader("Detailed order data")
st.caption(f"Showing {len(f):,} filtered order records.")
st.dataframe(f.drop(columns=["Month","Year","Profit_Margin"]),use_container_width=True,hide_index=True)
st.download_button("Download filtered data (CSV)",f.drop(columns=["Month","Year","Profit_Margin"]).to_csv(index=False).encode("utf-8"),
                   file_name="retail_sales_filtered.csv",mime="text/csv")
st.caption("Portfolio project | Dataset is synthetic and created for demonstration and interview practice.")
