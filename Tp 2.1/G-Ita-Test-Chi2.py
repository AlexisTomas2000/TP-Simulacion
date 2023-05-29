from numpy import number
import pandas as pd
import scipy.stats as stats
from matplotlib import pyplot
import numpy as np
import random

s1=1234
s2=2934
s0=6153
n=10000
numbers=[]
pn=int(abs(s2-s0))
numbers.insert(0,pn)

def fg(na):
    fnn=int(abs(n-(na*1.99)))
    return fnn

for i in range(1,1000):
    numbers.insert(i,fg(numbers[i-1]))

print(numbers)

co=[0,0,0,0,0,0,0,0,0,0]


for i in range(1,len(numbers)):
    if (numbers[i] >= 0 and numbers[i] <= 999):
        co[0]=co[0] + 1
    elif (numbers[i] >= 1000 and numbers[i] <= 1999):
        co[1]=co[1] + 1
    elif (numbers[i] >= 2000 and numbers[i] <= 2999):
        co[2]=co[2] + 1
    elif (numbers[i] >= 3000 and numbers[i] <= 3999):
        co[3]=co[3] + 1
    elif (numbers[i] >= 4000 and numbers[i] <= 4999):
        co[4]=co[4] + 1
    elif (numbers[i] >= 5000 and numbers[i] <= 5999):
        co[5]=co[5] + 1
    elif (numbers[i] >= 6000 and numbers[i] <= 6999):
        co[6]=co[6] + 1
    elif (numbers[i] >= 7000 and numbers[i] <= 7999):
        co[7]=co[7] + 1
    elif (numbers[i] >= 8000 and numbers[i] <= 8999):
        co[8]=co[8] + 1
    elif (numbers[i] >= 9000 and numbers[i] <= 9999):
        co[9]=co[9] + 1


df = pd.Series(numbers).value_counts() 
print('df')
print(df) 

print(sum(df))

print(stats.chisquare(f_obs =co))

print(co)

def chi_cuadrado(co):
    for i in range(0,10):
        print('Calculo para', i, ((co[i] - 100)**2)/100)

chi_cuadrado(co)