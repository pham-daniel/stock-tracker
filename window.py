import streamlit as st
from stock import Backend

class Frontend:
    if "initial_run" not in st.session_state:
        st.session_state.initial_run = True
        st.session_state.refresh_overview = True
    if "search_query" not in st.session_state:
        st.session_state.search_query = "NVDA"
    if "graph_period" not in st.session_state:
        st.session_state.graph_period = "1d"
    if "graph_type" not in st.session_state:
        st.session_state.graph_type = "Line"
    if "search_triggered" not in st.session_state:
        st.session_state.search_triggered = False


    tab1,tab2,tab3 = st.tabs(["Stock Overview","Stock Search","News"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Refresh", type="primary"):
                st.session_state.refresh_overview = True
                st.rerun()
                
        st.header("Global Indices")
        if st.session_state.refresh_overview:
            with st.container():
                col1, col2, col3 = st.columns(3,border=True)
                col4, col5, col6 = st.columns(3,border=True)
                with col1:
                    Backend.init_tab("^DJI","1 day")
                with col2:
                    Backend.init_tab("^IXIC","1 day")
                with col3:
                    Backend.init_tab("^GSPC","1 day")
                with col4:
                    Backend.init_tab("^HSI","1 day")
                with col5:
                    Backend.init_tab("^AXJO","1 day")
                with col6:
                    Backend.init_tab("^N225","1 day")

            st.header("Index Futures")
            with st.container():
                col1, col2, col3 = st.columns(3,border=True)
                col4, col5, col6 = st.columns(3, border=True)
                with col1:
                    Backend.init_tab("YM=F","1 day")
                with col2:
                    Backend.init_tab("NQ=F","1 day")
                with col3:
                    Backend.init_tab("ES=F","1 day")
                with col4:
                    Backend.init_tab("^VIX","1 day")
                with col5:
                    Backend.init_tab("RTY=F","1 day")
                with col6:
                    Backend.init_tab("NIY=F","1 day")

            st.header("Commodites")
            with st.container():
                col1, col2, col3 = st.columns(3,border=True)
                with col1:
                    Backend.init_tab("CL=F","1 day")
                with col2:
                    Backend.init_tab("GC=F","1 day")
                with col3:
                    Backend.init_tab("NG=F","1 day")   
                    

            st.header("Bonds")
            with st.container():
                col1, col2, col3 = st.columns(3,border=True)
                with col1:
                    Backend.init_tab("^FVX","1 day")
                with col2:
                    Backend.init_tab("^TNX","1 day")
                with col3:
                    Backend.init_tab("^TYX","1 day")   
                    
            st.header("Crypto")
            with st.container():
                col1, col2, col3 = st.columns(3,border=True)
                with col1:
                    Backend.init_tab("BTC-USD","1 day")
                with col2:
                    Backend.init_tab("ETH-USD","1 day")
                with col3:
                    Backend.init_tab("SOL-USD","1 day")
            st.session_state.refresh_overview = False
            
    with tab2: 
        search_input = st.text_input("Enter a stock to search:", value=st.session_state.search_query, key="search_input")
        graph_period = st.selectbox(
            "Period of Graph:",
            ("1 day", "5 days", "1 month", "6 months", "1 year", "5 years","Max")
        )
        graph_type = st.selectbox(
            "Graph Type:",
            ("Line","Candlestick")
        )
        if st.button("Search", key="search_button"):
            st.session_state.search_query = search_input.upper()
            st.session_state.graph_period = graph_period
            st.session_state.graph_type = graph_type
            st.session_state.search_triggered = True
            st.rerun() 

        if st.session_state.search_triggered:
            try:
                Backend.init_tab(st.session_state.search_query,st.session_state.graph_period)
            except Exception as e:
                st.error(f"Error: {e} Ensure the ticker is spelt correctly.")
            st.session_state.search_triggered = False
            with st.container():
                open,high,yearly_high,pe_ratio,revenue_per_share,today_volume,low,yearly_low,dividend_yield,market_cap = Backend.get_stats(st.session_state.search_query)
                col1,col2 = st.columns(2)
                with col1:
                    st.write("Open")
                    st.caption(f"${round(open,2)}")
                    st.write("High")
                    st.caption(f"${round(high,2)}")
                    st.write("52 week high")
                    st.caption(f"${round(yearly_high,2)}")
                    st.write("P/E Ratio")
                    st.caption(f"{round(pe_ratio,2)}")
                    st.write("Earnings Per Share")
                    st.caption(f"${round(revenue_per_share,2)}")
                with col2:
                    st.write("Today's Volume")
                    st.caption(f"${today_volume}")
                    st.write("Low")
                    st.caption(f"${round(low,2)}")
                    st.write("52 week low")
                    st.caption(f"${round(yearly_low,2)}")
                    st.write("Dividend Yield")
                    st.caption(f"{round(dividend_yield,2)}%")
                    st.write("Market Cap")
                    st.caption(f"${market_cap}")
    
    with tab3:
        news_search_input = st.text_input("Enter a stock to search for news:", value=st.session_state.search_query, key="news_search_input")
        
        if "news_search_triggered" not in st.session_state:
            st.session_state.news_search_triggered = False
            
        if st.button("Search", key= "news_search"):
            st.session_state.search_query = news_search_input.upper()
            st.session_state.news_search_triggered = True   
            st.rerun() 
            
        if st.session_state.news_search_triggered:
            try:
                ticker_news = Backend.get_ticker_news(st.session_state.search_query)
                st.session_state.search_triggered = False
            except Exception as e:
                st.error(f"Error: {e} Ensure the ticker is spelt correctly.")
                st.session_state.search_triggered = False
                ticker_news = []
            
            for article in ticker_news:
                col1, col2 = st.columns([3,2])
                with col1:
                    st.write(f"### [{article['content']['title']}]({article['content']['canonicalUrl']['url']})")
                    st.text(article['content']['summary'])
                with col2:
                    try:
                        st.image(article['content']['thumbnail']['originalUrl'])
                    except:
                        pass 