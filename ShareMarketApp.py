import streamlit as st
import datetime
import yfinance as yf

ticker_symbol = st.text_input("Enter the stock symbol","AAPL")


# python -m venv .venv
 #.\.venv\Scripts\activate



import streamlit as st

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Start date", datetime.date(2019, 7, 6))

with col2:
    end_date = st.date_input("end date", datetime.date(2023, 7, 6))


Data = yf.download(ticker_symbol,start = start_date, end=end_date)

st.write(Data)

st.line_chart(Data["Close"])
