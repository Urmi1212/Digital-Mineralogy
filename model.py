# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 21:21:51 2022

@author: Urmi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# Import Regression models
from sklearn.ensemble import RandomForestRegressor

#Read dataset
data0 = pd.read_csv("./_data0.csv", low_memory=False)
data1 = pd.read_csv("./_data1.csv", low_memory=False)
data2 = pd.read_csv("./_data2.csv", low_memory=False)

#Since we have a very small dataset, we will train our model with all availabe data.
import sklearn
data0=sklearn.utils.shuffle(data0)
data1=sklearn.utils.shuffle(data1)
data2=sklearn.utils.shuffle(data2)
x1 = data0[0:int(data0.shape[0]*1)] 
x2 = data1[0:int(data0.shape[0]*1)] 
x3 = data2[0:int(data2.shape[0]*1)]
Data_Train = np.vstack((x1,x2,x3))


Data_Train_X = Data_Train[:, 0:39]
Data_Train_Y = Data_Train[:,-1]

feature_names=data0.columns[1:39]
#Random Forest
model = RandomForestRegressor(bootstrap=True, ccp_alpha=0.0, criterion='mse',
                                max_depth=None, max_features=None, max_leaf_nodes=50,
                                max_samples=None, min_impurity_decrease=0.0,
                                min_samples_leaf=1,
                                min_samples_split=2, min_weight_fraction_leaf=0.0,
                                n_estimators=300, n_jobs=-1, oob_score=True,
                                random_state=20, verbose=0, warm_start=False)


model.fit(Data_Train_X,Data_Train_Y)


# Saving model to disk
pickle.dump(model, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[37.5435, 9.2736, 9.7701, 0.3667, 0.1752, 3.2236, 0.132,	0.1164,	2.2743,	0.1185,	0.8694,	0.7077,	0.7838,	2.5091,	0.2516,	3.0542,	2.834,	0.0857,	0.3728,	0.3242,	0.7025,	0.7364,	19.5873, 0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	8.0634887,	1]]))


