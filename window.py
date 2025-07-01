import streamlit as st
from stock import Backend

class Frontend:
    if "initial_run" not in st.session_state:
        st.session_state.initial_run = True
        st.session_state.refresh_overview = True
    if "search_triggered" not in st.session_state:
        st.session_state.search_triggered = False


    tab1,tab2 = st.tabs(["Stock Overview","Stock Search"])

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