#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


import yfinance as yf


# In[4]:


msft = yf.Ticker("MSFT")


# In[5]:


msft.info


# In[6]:


hist = msft.history(period="1mo")


# In[7]:


# show meta information about the history (requires history() to be called first)
msft.history_metadata


# In[8]:


# actions for (dividends, splits, capital gains)
msft.actions
msft.dividends
msft.splits
msft.capital_gains


# In[9]:


# share count
msft.get_shares_full(start="2022-01-01", end=None)


# In[10]:


# financials:
msft.calendar
msft.sec_filings
# income statement
msft.income_stmt
msft.quarterly_income_stmt
# balance sheet
msft.balance_sheet
msft.quarterly_balance_sheet
# cash flow statement
msft.cashflow
msft.quarterly_cashflow
# Ticker.get_income_stmt()` for more options


# In[11]:


# All holders
msft.major_holders
msft.institutional_holders
msft.mutualfund_holders
msft.insider_transactions
msft.insider_purchases
msft.insider_roster_holders


# In[12]:


msft.sustainability

# recommendations
msft.recommendations
msft.recommendations_summary
msft.upgrades_downgrades


# In[13]:


# analysts data:
msft.analyst_price_targets
msft.earnings_estimate
msft.revenue_estimate
msft.earnings_history
msft.eps_trend
msft.eps_revisions
msft.growth_estimates


# In[14]:


msft.earnings_dates


# In[16]:


#ISIN = International Securities Identification Number
msft.isin


# In[17]:


msft.options


# In[18]:


msft.news


# In[34]:


#option chain for specific expiration
opt = msft.option_chain('2024-11-01')

# Display the call and put options
calls = opt.calls
puts = opt.puts

print("Calls:\n", calls)
print("Puts:\n", puts)


# In[36]:


msftspy = yf.Ticker('SPY')
data = spy.funds_data


# In[37]:


data.description


# In[38]:


data.fund_overview
data.fund_operations


# In[39]:


# holdings related information
data.asset_classes
data.top_holdings
data.equity_holdings
data.bond_holdings
data.bond_ratings
data.sector_weightings


# In[40]:


data = yf.download("SPY AAPL", period="1mo")


# In[41]:


tech = yf.Sector('technology')
software = yf.Industry('software-infrastructure')
tech.key
tech.name
tech.symbol
tech.ticker
tech.overview
tech.top_companies
tech.research_reports
tech.top_etfs
tech.top_mutual_funds
tech.industries


# In[42]:


software.sector_key
software.sector_name
software.top_performing_companies
software.top_growth_companies


# In[46]:


pip install nospam


# In[47]:


import yfinance as yf
yf.set_tz_cache_location("custom/cache/location")
...


# In[ ]:




