import yfinance as yf
import plotly.graph_objs as go
import streamlit as st

class Backend:

    def get_ticker_info(ticker):
        ticker_info = yf.Ticker(ticker).info
        name = ticker_info.get("longName") or ticker_info.get("shortName")
        price = round(ticker_info.get("regularMarketPrice"),2)
        prev_close = ticker_info.get("previousClose")
        price_diff = ticker_info.get("regularMarketChange")
        percent_diff = ticker_info.get("regularMarketChangePercent")
        st.subheader(f"{name}")
        st.metric(label=".",value=price,delta=f"{round(price_diff,2)} | {round(percent_diff,2)}%",label_visibility="collapsed")
        return price, prev_close

