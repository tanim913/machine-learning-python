  
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading dataset
dataset = pd.read_csv('50_Startups.csv')

#distiguishing independent and dependant data
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values

#Encode catagorial data 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder 
from sklearn.compose import ColumnTransformer
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
ct = ColumnTransformer([("Country", OneHotEncoder(),[3])], remainder= 'passthrough')
X = ct.fit_transform(X)

#Avoiding dummy variable trap
X = X[:, 1:]

#splitting dataset into training set and test set 
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split (X,Y, test_size= 0.2,random_state = 0)

#fitting multiple linear regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

#predicting the test sets result 
Y_pred = regressor.predict(X_test)

#building the optimal model using Backward elimination
import statsmodels.api as sm
X = np.append(arr =  np.ones((50,1)).astype(int), values = X, axis = 1)
X_opt = np.array(X[:, [0, 1, 2, 3, 4, 5]], dtype=float)
regressor_OLS = sm.OLS(endog = Y, exog = X_opt).fit()
print(regressor_OLS.summary())
X_opt = np.array(X[:, [0, 1, 3, 4, 5]], dtype=float)
regressor_OLS = sm.OLS(endog = Y, exog = X_opt).fit()
print(regressor_OLS.summary())
X_opt = np.array(X[:, [0 , 3, 4, 5]], dtype=float)
regressor_OLS = sm.OLS(endog = Y, exog = X_opt).fit()
print(regressor_OLS.summary())
X_opt = np.array(X[:, [0, 3, 5]], dtype=float)
regressor_OLS = sm.OLS(endog = Y, exog = X_opt).fit()
print(regressor_OLS.summary())
X_opt = np.array(X[:, [0, 3]], dtype=float)
regressor_OLS = sm.OLS(endog = Y, exog = X_opt).fit()
print(regressor_OLS.summary())
