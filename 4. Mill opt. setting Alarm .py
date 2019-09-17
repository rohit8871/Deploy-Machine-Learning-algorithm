
# coding: utf-8

# # Setting Alarm

# In[3]:


import timeseries as ts
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
import scipy
import statsmodels.api as sm
import pickle


# In[4]:


# Restoring pickle 
df_reg,df_forcast= pickle.load(open("Real_time_data.pkl", 'rb'))
listA,listB,listC,listD,listE= pickle.load(open("LIST.pkl", 'rb'))


# In[6]:


# Restore tuple from File 2
import pickle
model_millA,exoga,x_train_a_sub,y_train_a_sub,x_test_A,y_test_A,speed_A,current_A,model2_millA,MillA = pickle.load(open("pickle_model_millA.pkl", 'rb'))

model_millB,exogb,x_train_b_sub,y_train_b_sub,x_test_B,y_test_B,speed_B,current_B,model2_millB,MillB = pickle.load(open("pickle_model_millB.pkl", 'rb'))

model_millC,exogc,x_train_c_sub,y_train_c_sub,x_test_C,y_test_C,speed_C,current_C,model2_millC,MillC= pickle.load(open("pickle_model_millC.pkl", 'rb'))

model_millD,exogd,x_train_d_sub,y_train_d_sub,x_test_D,y_test_D,speed_D,current_D,model2_millD,MillD= pickle.load(open("pickle_model_millD.pkl", 'rb'))

model_millE,exoge,x_train_e_sub,y_train_e_sub,x_test_E,y_test_E,speed_E,current_E,model2_millE,MillE= pickle.load(open("pickle_model_millE.pkl", 'rb'))


# In[7]:


# Restore tuple from file 3
y_pred_a_sub,std_A= pickle.load(open("ModelA_pred_obj.pkl", 'rb'))

y_pred_b_sub,std_B= pickle.load(open("ModelB_pred_obj.pkl", 'rb'))

y_pred_c_sub,std_C= pickle.load(open("ModelC_pred_obj.pkl", 'rb'))

y_pred_d_sub,std_D= pickle.load(open("ModelD_pred_obj.pkl", 'rb'))

y_pred_e_sub,std_E= pickle.load(open("ModelE_pred_obj.pkl", 'rb'))


# ### Test of significance of Mill A

# ### setting an alarm

# In[8]:


# setting Alarm
# s == Acutal speed, c== Actual current
def alarm1_millA(s,c):
    print ("Actual_speed: "+ str(s.tolist()))
    print ("Actual_current: "+ str(c.tolist()))

    # Predicting current
    pred=model_millA.predict([1,s])
    print ('predicted current: '+str(pred))
    
    # Calculate Z score 
    z=(c -pred)/std_A
    print ('z score: '+str(z.tolist()))
    
    # calculate p-value
    import scipy
    p_value = scipy.stats.norm.sf(abs(z)) #one-sided
    print ('p_values: '+str(p_value))
    
    # Putting conditions on the basis of standard p-values (0.05)
    if (p_value < 0.05):
        print ('-----------------------------')
        print (' Actual current is insignificant')
        print ('-----------------------------')
        
        # Appending 1 after every iteration , to observe  5 consecutive insignificant results. 
        listA.append(1)
        slice=listA[-6:None]
        print ('list:'+str(listA[-10:None])+','+"last 6th value: "+str(slice))
        if sum(slice)>5:
            print ('')
            print ('====================================================')
            print ('Getting more than 5 consecutive Insignificant current')
            print ('Warning! Warning ! warning!')
            print ('====================================================')
            
        
    else:
        print ("current is significant 'No Alarm Required'")
        
        # Append 0 to indicate receiving  significant current
        listA.append(0)
        print (listA[-10:None])
    
    # to visualize the results.
    plt.scatter(speed_A,current_A,alpha = 0.02)
    plt.scatter(x_train_a_sub,model_millA.predict(exoga),alpha = 0.2)
    plt.scatter(x_train_a_sub,y_pred_a_sub-(0.6))
    plt.scatter(x_train_a_sub,y_pred_a_sub+0.6)
    plt.scatter(s,c, s=200,color = 'indigo')
    plt.grid()
    plt.title('Mill A')


# In[9]:


alarm1_millA(df_reg['FIQC_03305_A_FB'],df_reg['PULV_A_I'])


# ### Test of significance of Mill B

# ### setting an alarm

# In[27]:


# setting Alarm
# s == Acutal speed, c== Actual current
def alarm1_millB(s,c):
    print ("Actual_speed: "+ str(s.tolist()))
    print ("Actual_current: "+ str(c.tolist()))
    # Predicting current
    pred=model_millB.predict([1,s])
    print ('predicted current: '+str(pred))
    
    # Calculate Z score 
    z=(c -pred)/std_B
    print ('z score: '+str(z.tolist()))
    
    # calculate p-value
    import scipy
    p_value = scipy.stats.norm.sf(abs(z)) #one-sided
    print ('p_value: '+str(p_value))
    
    # Putting conditions on the basis of standard p-values (0.05)
    if (p_value < 0.05):
        print ('-----------------------------')
        print ('Getting insignificant current')
        print ('-----------------------------')

        # Appending 1 after every iteration , to observe  5 consecutive insignificant results. 
        listB.append(1)
        slice=listB[-6:None]
        print ('list:'+str(listB[-10:None])+','+"last 6th value: "+str(slice))
        if sum(slice)>5:
            print ('')
            print ('====================================================')
            print ('Getting more than 5 consecutive Insignificant current')
            print ('Warning! warning! warning!')
            print ('====================================================')
            
        
    else:
        print ("current is significant 'No Alarm Required'")
        
        # Append 0 to indicate receiving  significant current
        listB.append(0)
        print (listB[-10:None])
        
    # visualization
    plt.scatter(speed_B,current_B,alpha = 0.02)
    plt.scatter(x_train_b_sub,model_millB.predict(exogb),alpha = 0.2)
    plt.scatter(x_train_b_sub,y_pred_b_sub-0.62)
    plt.scatter(x_train_b_sub,y_pred_b_sub+0.62)
    plt.scatter(s,c, s=200,color = 'indigo')
    plt.grid()
    plt.title('Mill B')


# In[28]:


alarm1_millB(df_reg['FIQC_03305_B_FB'],df_reg['PULV_B_I'])


# ### Test of significance of Mill C

# ### setting an alarm

# In[29]:


# setting Alarm
# s == Acutal speed, c== Actual current
def alarm1_millC(s,c):
    print ("Actual_speed: "+ str(s.tolist()))
    print ("Actual_current: "+ str(c.tolist()))
    # predict current
    pred=model_millC.predict([1,s])
    print ('predicted current: '+str(pred))
    
    # calculate z score
    z=(c -pred)/std_C
    print ('z score: '+str(z.tolist()))
    
    # calculate p value
    import scipy
    p_value = scipy.stats.norm.sf(abs(z))*2 #one-sided
    print ('p_value: '+str(p_value))
    
    # Putting conditions on the basis of standard p-values (0.05)
    if (p_value < 0.05):
        print ('-----------------------------')
        print ('Getting insignificant current')
        print ('-----------------------------')
        
        # Appending 1 after every iteration , to observe  5 consecutive insignificant results. 
        listC.append(1)
        slice=listC[-6:None]
        print ('list:'+str(listC[-10:None])+','+"last 6th value: "+str(slice))
        if sum(slice)>5:
            print ('')
            print ('====================================================')
            print ('Getting more than 5 consecutive Insignificant current')
            print ('Warning! warning! warning!')
            print ('====================================================')
            
        
    else:
        print ("current is significant 'No Alarm Required'")
        # Append 0 to indicate receiving  significant current
        listC.append(0)
        print (listC[-10:None])
        
    # visualization
    plt.scatter(speed_C, current_C,alpha = 0.02)
    plt.scatter(x_train_c_sub,model_millC.predict(exogc),alpha = 0.2)
    plt.scatter(x_train_c_sub,y_pred_c_sub-0.52)
    plt.scatter(x_train_c_sub,y_pred_c_sub+0.52)
    plt.scatter(s,c, s=200,color = 'indigo')
    plt.grid()
    plt.title('Mill C')


# In[30]:


alarm1_millC(df_reg['FIQC_03305_C_FB'],df_reg['PULV_C_I'])


# ### =======================================================================================

# ### Test of significance of Mill D

# ### setting an alarm

# In[31]:


# setting an alarm
# s == Acutal speed, c== Actual current
def alarm1_millD(s,c):
    print ("Actual_speed: "+ str(s.tolist()))
    print ("Actual_current: "+ str(c.tolist()))
    # Predict current
    pred=model_millD.predict([1,s])
    print ('predicted current: '+str(pred))
    
    # calculate Z score
    z=(c -pred)/std_D
    print ('z score: '+str(z.tolist()))
    
    # calculate p value
    import scipy
    p_value = scipy.stats.norm.sf(abs(z))*2 #one-sided
    print ('p_value: '+str(p_value))
    
    # Putting conditions on the basis of standard p-values (0.05)
    if (p_value < 0.05):
        print ('-----------------------------')
        print ('Getting insignificant current')
        print ('-----------------------------')
        
        # Appending 1 after every iteration , to observe  5 consecutive insignificant results. 
        listD.append(1)
        slice=listD[-6:None]
        print ('list:'+str(listD[-10:None])+','+"last 6th value: "+str(slice))
        if sum(slice)>5:
            print ('')
            print ('====================================================')
            print ('Getting more than 5 consecutive Insignificant current')
            print ('Warning! warning! warning!')
            print ('====================================================')
            
        
    else:
        print ("current is significant 'No Alarm Required'")
        
        # Append 0 to indicate receiving  significant current
        listD.append(0)
        print (listD[-10:None])
        
    # visualization
    plt.scatter(speed_D,current_D,alpha = 0.02)
    plt.scatter(x_train_d_sub,model_millD.predict(exogd),alpha = 0.2)
    plt.scatter(x_train_d_sub,y_pred_d_sub-0.85)
    plt.scatter(x_train_d_sub,y_pred_d_sub+0.85)
    plt.scatter(s,c, s=200,color = 'indigo')
    plt.grid()
    plt.title('Mill D')


# In[32]:


alarm1_millD(df_reg['FIQC_03305_D_FB'],df_reg['PULV_D_I'])


# ### ======================================================================================

# ### Test of significance of Mill E

# ### setting an alarm

# In[33]:


# setting an alarm
# s == Acutal speed, c== Actual current
def alarm1_millE(s,c):
    print ("Actual_speed: "+ str(s.tolist()))
    print ("Actual_current: "+ str(c.tolist()))
    # predict current
    pred=model_millE.predict([1,s])
    print ('predicted current: '+str(pred))
    
    # calculate Z score
    z=(c -pred)/std_E 
    print ('z score: '+str(z.tolist()))
    
    # calculate p value
    import scipy
    p_value = scipy.stats.norm.sf(abs(z)) #one-sided
    print ('p_value: '+str(p_value))
    
    # Putting conditions on the basis of standard p-values (0.05)
    if (p_value < 0.05):
        print ('-----------------------------')
        print ('Getting insignificant current')
        print ('-----------------------------')
        
        # Appending 1 after every iteration , to observe  5 consecutive insignificant results. 
        listE.append(1)
        slice=listE[-6:None]
        print ('list:'+str(listE[-10:None])+','+"last 6th value: "+str(slice))
        if sum(slice)>5:
            print ('')
            print ('====================================================')
            print ('Getting more than 5 consecutive Insignificant current')
            print ('Warning! warning! warning!')
            print ('====================================================')
            
        
    else:
        print ("current is significant 'No Alarm Required'")
        
        # Append 0 to indicate receiving  significant current
        listE.append(0) 
        print (listE[-10:None])
        
    # visualization
    plt.scatter(speed_E, current_E,alpha = 0.02)
    plt.scatter(x_train_e_sub,model_millE.predict(exoge),alpha = 0.2)
    plt.scatter(x_train_e_sub,y_pred_e_sub-0.53)
    plt.scatter(x_train_e_sub,y_pred_e_sub+0.53)
    plt.scatter(s,c, s=200,color = 'indigo')
    plt.grid()
    plt.title('Mill E')


# In[34]:


alarm1_millE(df_reg['FIQC_03305_E_FB'],df_reg['PULV_E_I'])


# ### ====================================================================================
