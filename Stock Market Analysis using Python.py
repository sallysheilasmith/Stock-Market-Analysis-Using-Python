#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import yfinance as yf


# In[3]:


import yfinance as yf


# In[4]:


pip install yfinance 


# In[5]:


import yfinance as yf


# In[6]:


import datetime


# In[7]:


from datetime import date, timedelta


# In[8]:


import plotly.graph_objects as go


# In[9]:


import plotly.express as px


# In[10]:


today = date.today()


# In[11]:


d1 = today.strftime("%Y-%m-%d")


# In[12]:


end_date = d1


# In[13]:


d2 = date.today() - timedelta(days=365)


# In[14]:


d2 = d2.strftime("%Y-%m-%d")


# In[15]:


start_date = d2


# In[16]:


data = yf.download('GOOG', 
                      start=start_date, 
                      end=end_date, 
                      progress=False)


# In[17]:


data["Date"] = data.index


# In[18]:


data = data[["Date", "Open", "High", "Low", 
             "Close", "Adj Close", "Volume"]]


# In[19]:


data.reset_index(drop=True, inplace=True)
print(data.head())


# In[20]:


figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                        open=data["Open"], high=data["High"],
                                        low=data["Low"], close=data["Close"])])


# In[21]:


figure.update_layout(title = "Google Stock Price Analysis", xaxis_rangeslider_visible=False)
figure.show()


# In[22]:


figure = px.bar(data, x = "Date", y= "Close")


# In[23]:


figure.show()


# In[24]:


figure = px.line(data, x='Date', y='Close', 
                 title='Stock Market Analysis with Rangeslider')


# In[25]:


figure.update_xaxes(rangeslider_visible=True)


# In[26]:


figure.show()


# In[27]:


figure = px.line(data, x='Date', y='Close', 
2
                 title='Stock Market Analysis with Time Period Selectors')


# In[28]:


figure = px.line(data, x='Date', y='Close', 

                 title='Stock Market Analysis with Time Period Selectors')


# In[29]:


figure.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)


# In[30]:


figure.show()


# In[31]:


figure = px.scatter(data, x='Date', y='Close', range_x=['2021-07-12', '2022-07-11'],
                 title="Stock Market Analysis by Hiding Weekend Gaps")


# In[32]:


figure.update_xaxes(
    rangebreaks=[
        dict(bounds=["sat", "sun"])
    ]
)


# In[ ]:




