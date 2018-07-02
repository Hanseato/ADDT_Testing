import itertools
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib import style
#style.use('ggplot')

def expand_grid(data_dict):
    rows=itertools.product(*data_dict.values())
    return pd.DataFrame.from_records(rows, columns=data_dict.keys())

def YvalR(beta0, beta1, beta2,tempK,tau,sigma):
    mu = beta0+beta1*np.exp(beta2*(-11605/tempK))*tau
    R=np.random.normal(mu, sigma)
    val=R
    return val

def Yval(beta0, beta1, beta2,tempK,tau):
    mu = beta0+beta1*np.exp(beta2*(-11605/tempK))*tau
    val=mu
    return val

#Model Parameter Definition
beta0=4.471
beta1=-8.641*np.power(10,8)
beta2=0.6364
tempC=np.array([50, 60,70])
tempK=tempC+273.15
time= np.array([2.0,4.0,6.0,12.0,16.0])
ModTime=np.arange(0,16,0.1)
samples=np.arange(1,6)
tau=np.round(np.sqrt(time),5)
ModTau=np.round(np.sqrt(ModTime),5)
sigma=0.1580

data_dict = {'Temperature': tempK, 'Tau': tau, 'Sample': samples}
df=expand_grid(data_dict)
#print(df)
#generate simulated measures
Meas = [YvalR(beta0, beta1,beta2, df.iloc[i]['Temperature'], df.iloc[i]['Tau'],sigma)for i in range(len(df))]
#add Meas to data frame df
df['Measures']= Meas
#print(df)

M1=df.loc[lambda df: df.Temperature==tempK[0],:]
M2=df.loc[lambda df: df.Temperature==tempK[1],:]
M3=df.loc[lambda df: df.Temperature==tempK[2],:]

Y1= Yval(beta0, beta1,beta2,tempK[0],ModTau)
Y2= Yval(beta0, beta1,beta2,tempK[1],ModTau)
Y3= Yval(beta0, beta1,beta2,tempK[2],ModTau)

#print(Y1)
plt.grid(True,'k')
plt.scatter(x=np.power(M1.loc[:]['Tau'],2), y=np.exp(M1.loc[:]['Measures']), color='k')
plt.scatter(x=np.power(M2.loc[:]['Tau'],2), y=np.exp(M2.loc[:]['Measures']),color='c')
plt.scatter(x=np.power(M3.loc[:]['Tau'],2), y=np.exp(M3.loc[:]['Measures']),color='g')
plt.plot(x=np.power(ModTau,2), y=np.exp(Y1), color='k')
plt.plot(x=np.power(ModTau,2), y=np.exp(Y2), color='c', linewidth=5)
plt.plot(x=np.power(ModTau,2), y=np.exp(Y3), color='g',linewidth=5)

plt.title('Simulated Degradation Measurements')
plt.xlabel('Time in weeks')
plt.ylabel('Performance in %')
plt.show()

#save data
filename="measurements.txt"
file=open(filename, 'wb')
pickle.dump(df, file)
#read data

#file=open(filenam, 'rb')
#df1=pickle.load(file)