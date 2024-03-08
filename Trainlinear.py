from math import inf 
from collections import Counter
from state import UltimateTTT_Move
import copy
from timeit import default_timer as timer
import random
import numpy as np
import pandas as pd

def model(X, Y, learning_rate, iteration):
  m = Y.size
  theta = np.zeros((X.shape[1], 1))
  cost_list = []
  for i in range(iteration):
    y_pred = np.dot(X, theta)
    cost = (1/(2*m))*np.sum(np.square(y_pred - Y))
    d_theta = (1/m)*np.dot(X.T, y_pred - Y)
    theta = theta - learning_rate*d_theta
    cost_list.append(cost)
    # to print the cost for 10 times
    if(i%(iteration/10) == 0):
      print("Cost is :", cost)
  return theta, cost_list

df = pd.read_csv('D:\Data.csv') 
  
print(df.head()) 
print(df.columns)

X=df.values[:,1:]
Y=df.values[:,0].reshape(df.shape[0],1)
coef,cost=model(X,Y,0.5,10000)
print(coef)
print(len(coef))