import streamlit as st
import datetime
import yfinance as yf

ticker_symbol = st.text_input("Enter the stock symbol","AAPL")


start_date = st.date_input("Start date", datetime.date(2019, 7, 6))
end_date = st.date_input("end date", datetime.date(2023, 7, 6))


Data = yf.download(ticker_symbol,start = start_date, end=end_date)

st.write(Data)