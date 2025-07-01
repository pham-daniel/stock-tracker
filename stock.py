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


    def create_candlestick_chart(ticker,period,interval):
        fig = go.Figure()
        stock_data = yf.download(ticker, period=period,interval=interval)
        fig.add_trace(go.Candlestick(
        x = stock_data.index,
        open=stock_data['Open',ticker], 
        high=stock_data['High',ticker],  
        low=stock_data['Low',ticker],
        close=stock_data['Close',ticker],
        increasing=dict(line=dict(color='green'), fillcolor='green'),
        decreasing=dict(line=dict(color='red'), fillcolor='red')
        ))
        return fig

    
    def create_line_chart(ticker, price, prev_close,period,interval):
        fig = go.Figure()
        stock_data = yf.download(ticker, period=period,interval=interval)
        line_color = "green" if price >= prev_close else "red"
        fig.add_trace(go.Scatter(
        x = stock_data.index,
        y = stock_data["Close",ticker],
        mode='lines',
        line=dict(color=line_color),
        ))
        return fig
    
    @staticmethod
    def init_tab(ticker,period):
        interval = {
            "1d": "5m",
            "5d": "5m",
            "1mo": "30m",
            "6mo": "1d",
            "1y": "1d",
            "5y": "7d",
            "max": "1mo",
        }
        period_convert = {
            "1 day": "1d",
            "5 days": "5d",
            "1 month": "1mo",
            "6 months": "6mo",
            "1 year": "1y",
            "5 years": "5y",
            "Max": "max",    
        }
        price, prev_close = Backend.get_ticker_info(ticker)
        if st.session_state.graph_type == "Line" or st.session_state.refresh_overview:
            fig = Backend.create_line_chart(ticker,price, prev_close,period_convert[period],interval[period_convert[period]])
            fig.update_layout(
                xaxis=dict(type='category',showticklabels=False,showgrid=False,zeroline=False), 
                yaxis=dict(showticklabels=False,showgrid=False,zeroline=False)
            )

            if st.session_state.refresh_overview:
                st.plotly_chart(fig,key=ticker,config={
                "staticPlot": True
        })
            else:
                st.plotly_chart(fig,key=ticker)

        elif st.session_state.graph_type == "Candlestick":
            fig = Backend.create_candlestick_chart(ticker,period_convert[period],interval[period_convert[period]])
            fig.update_layout(
                xaxis=dict(type='category',showticklabels=False,showgrid=False,zeroline=False)
            )
            st.plotly_chart(fig,key=ticker)