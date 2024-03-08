
from math import inf 
import numpy as np
import pandas as pd

def sigmoid(x):
    return 1/(1 + np.exp(-x))
def safe_log(x):
    if np.isnan(np.log(x)).all():
        return 0
    else:
        return np.log(x)
def model(X, Y, learning_rate, iterations):
    
    m = X.shape[1]
    n = X.shape[0]
    
    W = np.zeros((n,1))
    B = 0
    
    cost_list = []
    
    for i in range(iterations):
        
        Z = np.dot(W.T, X) + B
        A = sigmoid(Z)
        
        # cost function
        cost = -(1/m)*np.sum( Y*safe_log(A) + (1-Y)*safe_log(1-A))
        
        # Gradient Descent
        dW = (1/m)*np.dot(A-Y, X.T)
        dB = (1/m)*np.sum(A - Y)
        
        W = W - learning_rate*dW.T
        B = B - learning_rate*dB
        
        # Cost function value
        cost_list.append(cost)
        
        if(i%(iterations/10) == 0):
            print("cost after ", i, "iteration is : ", cost)
    return W, B, cost_list

df = pd.read_csv('D:\Data.csv') 
print(df.head()) 
print(df.columns)
X=df.values[:,1:]
Y=df.values[:,0].reshape(df.shape[0],1)
print(X.shape[0])
X=X.T
Y=Y.T
iterations = 100000000
learning_rate = 0.01
W, B, cost_list = model(X, Y, learning_rate = learning_rate, iterations = iterations)
print(W)