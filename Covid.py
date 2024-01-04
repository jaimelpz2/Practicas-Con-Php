# -*- coding: utf-8 -*-
#SE pretende calcular los dias que pasa un paciente
# de covid para ser hospitalizado siendo entonces
#nuestra variable aleatoria:
#numero de dias desde el primer sintoma a ser
#hospitalizado

"""
Created on Sun Jun 13 19:01:11 2021

@author: JimmyLpz
"""

#from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
import seaborn as sns



def generator(a,c,m,xi):
	return ((a*xi)+c)%m

def n_random_numbers(a,c,m,seed,n):
	r = []
	xi = [0,seed]
	for i in range(1,n+1):
		 xi1 = generator(a,c,m,xi[i])
		 xi.append(xi1)
		 r.append(xi1/(m-1))
	return r

def all_random_numbers(a,c,m,seed):
	r = []
	xi = [0,seed]
	i = 1
	unique_xis = dict()
	while(xi[i] not in unique_xis):
		 xi1 = generator(a,c,m,xi[i])
		 xi.append(xi1)
		 unique_xis[xi[i]] = True
		 r.append(xi1/(m-1))
		 i+=1
	return r
	

def period(a,c,m,seed):
	return len(all_random_numbers(a, c, m, seed))


generatorValues2 = {
		'a': 16807,
		'c': 0,
		'm': 2147483647,
		'seed': 1,
        'n': 1100
	}

ar=(n_random_numbers(**generatorValues2))
ed=.95

df=pd.read_excel('Covid.xlsx')
#df2=pd.read_excel('Covid2.xlsx')

#print(df.info())

#print(df.describe())

pd.set_option('display.max_rows',1500)

#df['Fecha_Ingreso']=df['Fecha_Ingreso'].map(lambda x: convert_date(x))

df['DiasParaHospitalizar']=df['FECHA_INGRESO'] - df['FECHA_SINTOMAS']

print("\n",df['DiasParaHospitalizar'])

new_df=df['DiasParaHospitalizar']
x=(new_df / np.timedelta64(1,'D')).astype(int)
print("\n",x.describe()[['mean','std','count']])
a=np.mean(x)
print("variance",np.var(x))

#print(new_df.dtypes)

hist=df['DiasParaHospitalizar'].dt.days.hist(bins=int(np.sqrt(df.shape[0])))

plt.show()

print("Distrubution: Exponential",expon.rvs(x,a))
print("\n\nHistoric information\n\n\n")

print("New information")
print("\n\n",ar)

print("\n\nMean:",np.mean(ar))
print("Std:",np.std(ar))
print("variance:",np.var(ar))
b=np.mean(ar)
des=expon.rvs(ar)

ax=sns.distplot(des,kde=True,color='skyblue',hist_kws={"linewidth":25, 'alpha':1})
plt.show()
