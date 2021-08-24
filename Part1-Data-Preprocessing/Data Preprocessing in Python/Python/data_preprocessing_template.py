import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values

Y = dataset.iloc[:, 3].values

#taking care of missing data
from sklearn.impute import SimpleImputer
     
imputer = SimpleImputer(missing_values= np.NAN, strategy= 'mean')

imputer.fit(X[:, 1:3])

X[:, 1:3] = imputer.transform(X[:, 1:3])

#Encode catagorial data 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder 
from sklearn.compose import ColumnTransformer

labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

ct = ColumnTransformer([("Country", OneHotEncoder(),[0])], remainder= 'passthrough')

X = ct.fit_transform(X)

labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)


 

    
