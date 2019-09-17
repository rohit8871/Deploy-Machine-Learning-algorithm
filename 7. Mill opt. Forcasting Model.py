
# coding: utf-8

# In[605]:


import timeseries as ts
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import warnings
warnings.filterwarnings("ignore")
import pickle


# In[606]:


# Restoring pickle 
df_reg,df_forcast= pickle.load(open("Real_time_data.pkl", 'rb'))
Mythresholds= pickle.load(open("mythresholds.pkl", 'rb'))


# In[608]:


def forecasting(real_time_data):
    # Import library
    from statsmodels.tsa.api import Holt
    
    # Extract out the Thresholds from the Dictionary
    tag = ''.join((pd.DataFrame(real_time_data).columns).tolist())
    lower_thr=Mythresholds[tag]['val_lower']
    print ('val_lower: '+str(lower_thr))
    upper_thr=Mythresholds[tag]['val_upper'] 
    print ('val_upper: '+str(upper_thr))
    print ('')
    # dataset for training exponential smoothing
    if len(real_time_data) >1:
        fit = Holt(real_time_data, damped=True).fit(smoothing_level=0.2, smoothing_slope=0.04)
        fcast = fit.forecast(8).rename("Forcasted value")
        print ('Forcasted value: '+ str(fcast.tolist()))
        print ('------------------------------------------------------------------------------------------------------------------')
        plt.figure(figsize=[20,5])
        fit.fittedvalues.plot(color='green')
        fcast.plot(color='indigo',legend=True)
        plt.plot(real_time_data,color="black")
        plt.axhline(upper_thr, color ='red',linestyle='--')
        plt.axhline(lower_thr, color ='red',linestyle='--')
        plt.grid()
              
            
    # Behaviour of data in real time
    current_value = real_time_data[len(real_time_data)-1]
    print ('Actual current_value: ' +str(current_value))
    # calculate & storing change after every iteration    
    if len(real_time_data)>1:
        current_value = real_time_data[len(real_time_data)-1]
        previous_value = real_time_data[len(real_time_data)-2]
        change = current_value - previous_value
        
    # percentage change after every iteration
    if len(real_time_data) >1:
        current_perc=round((change/(upper_thr-lower_thr))*100,2)
        storing_percentage_value.append(current_perc)
            
        if (current_perc >10):
            print ('The change in % has been seen more than 10% in last hours :' +str(current_perc) +' %')
          
        else:
            print ('The Change in % has been seen in last hours is  :' +str(current_perc) +' %')
        storing_percentage_value_last5 = np.array(storing_percentage_value[-5:None])
        print ("last five change in percentage every hour: "+str(storing_percentage_value_last5)+' %')

    #def forcasted_perc_change(last,df):
    if len(real_time_data)>1:

        current_value = real_time_data[len(real_time_data)-1]
        forcast_perc_change=((fcast.tolist()[7]-current_value)/(upper_thr - lower_thr))*100
        print ('')
        print ('The % change has been seen in forcasted value : '+ str(round(forcast_perc_change,2))+' %')
        
        # Behaviour of forcasted data in real time
        if ((fcast.tolist()[7] > lower_thr) and (fcast.tolist()[7] < upper_thr)):
            print ('The forcasted value is within range: '+str(round(fcast.tolist()[7],2)))

        else:
            print ("Warning! warning! warning! .....")
            print ('-------------------------------------------------')
        
        # Calculate after what time variable will cross the thresholds. 
        for i in fcast:
            if i>=upper_thr:
                max=(fcast.tolist().index(i)+1)
                min=(fcast.tolist().index(i))
                if current_value < upper_thr:
                    print ("The actual value will cross upper threshold in "+str(min)+'-'+str(max)+ ' hours')
                else:
                    print ('The actual value has already been crossed upper threshold')
                    print ('Please take action immediately ')
                break
                
            if i<=lower_thr:
                max=(fcast.tolist().index(i)+1)
                min=(fcast.tolist().index(i))
                if current_value > llower_thrr_thr:
                    print ("The actual value will cross lower threshold in "+str(min)+'-'+str(max)+ ' hours')
                else:
                    print ('The actual value has already been crossed lower threshold')
                    print ('Please take action immediately ')
                break
               


# ### Model Prediction

# In[613]:


forecasting(df_forcast.PULV_D_I)

