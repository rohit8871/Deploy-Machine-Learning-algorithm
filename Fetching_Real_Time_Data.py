
# coding: utf-8

# In[1]:


import timeseries as ts
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
import pickle

context = "https://hindalco.exactspace.co/exactapi/tagmeta?filter={%22where%22:{%22equipmentType%22:%22Bowl%20Mill%22,%20%22measureType%22:{%22inq%22:[%22Current%22,%22Speed%22,%22Temperature%22,%22Pressure%22]}}}"
context = "https://hindalco.exactspace.co/exactapi/tagmeta?filter={%22where%22:{%22equipmentType%22:%22Bowl%20Mill%22}}"
tags = requests.get(context).json()
tag_list = []
for tag in tags:
    try:
        if(tag["measureType"] == "Current" or tag["measureUnit"]=="RPM") or True:
            tag_list.append(tag["dataTagId"])
            tag_list.append(tag["description"])
    except:
        pass
       
(tag_list)


# In[9]:


# Fetching data for forcasting file
qr = ts.timeseriesquery()
qr.addMetrics(list(set(tag_list)))
qr.chooseTimeType("relative",{"start_unit":"hours","start_value":"1"})
qr.addAggregators([{"name":"avg","sampling_unit":"hours","sampling_value":10}])
qr.submitQuery()
qr.formatResultAsDF()
df_regr = qr.resultset["results"][0]["data"]
df_regr["date"]=pd.to_datetime(df_regr["time"],unit="ms")
df_regr=df_regr.dropna()
df_regr.shape


# In[13]:


# Fetching data for forcasting file
qr = ts.timeseriesquery()
qr.addMetrics(list(set(tag_list)))
qr.chooseTimeType("relative",{"start_unit":"hours","start_value":"72"})
qr.addAggregators([{"name":"avg","sampling_unit":"hours","sampling_value":1}])
qr.submitQuery()
qr.formatResultAsDF()
df_forcasting = qr.resultset["results"][0]["data"]
df_forcasting["date"]=pd.to_datetime(df_forcasting["time"],unit="ms")
df_forcasting=df_forcasting.dropna()
df_forcasting.shape


# In[14]:


# Pickling objects
tuple_objects = (df_regr,df_forcasting)
pickle.dump(tuple_objects, open("Real_time_data.pkl", 'wb'))
# # Restore tuple
df_reg,df_forcast= pickle.load(open("Real_time_data.pkl", 'rb'))

