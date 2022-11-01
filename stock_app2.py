import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime

st.markdown('''
# This is a stock price application
### Select a stock company on the panel to get stock details
''')
st.write('---')

st.sidebar.subheader('Select a stock')
start_date = st.sidebar.date_input('Start date', datetime.date(2021,1,1))
end_date = st.sidebar.date_input('End date', datetime.date(2022,1,1))

ticker_list = pd.read_csv('symbols.csv')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list)
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)
string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

st.subheader('*Price chart*')
qf=cf.QuantFig(tickerDf,title=string_name,legend='top',name='Close prices')
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)
st.write('---')

st.subheader('*Stock financial data*')
st.write(tickerDf)
st.write('---')

string_summary = tickerData.info['longBusinessSummary']
st.info(string_summary)


