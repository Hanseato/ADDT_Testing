import numpy as np
import pandas as pd
import itertools

def expand_grid(data_dict):
    rows=itertools.product(data_dict.values())
    return pd.DataFrame.from_records(rows, columns= data_dict.keys())

def Yval(beta0, beta1, beta2,tempK,tau,sigma):
    mu = beta0+beta1*np.exp(beta2*(-11605/tempK))*tau
    R=np.random.normal(mu, sigma)
    val=mu+R
    return val

#Model Parameter Definition
beta0=4.471
beta1=-8.641*np.power(10,8)
beta2=0.6364
tempC=np.array([50, 60,70])
tempK=tempC+273.15
time= np.array([0.0,2.0,4.0,6.0,12.0,16.0])
tau=np.round(np.sqrt(time),5)
sigma=0.1580

data_dict = {'Temperature': tempK, 'Tau': tau}
df=expand_grid(data_dict)

#generate measures
