import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading dataset
dataset = pd.read_csv('Position_Salaries.csv')

#distiguishing independent and dependant data
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values

#splitting dataset into training set and test set 
'''from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split (X,Y, test_size= 0.2,random_state = 0)

#feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
'''



#fitting the regression model to the data set

#create regessor here


#predicting a new result with Polynomial Regression
Y_pred = regressor.predict([[6.5]])

#visualing the linear regreesion model

#visualing the regreesion model
plt.scatter(X, Y, color = "red")
plt.plot(X, regressor.predict(X), color = "blue")
plt.title('Truth of bluff( Regression Model)')
plt.xlabel('Position level ')
plt.ylabel('Salary')
plt.show()

#visualing the regreesion model (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, Y, color = "red")
plt.plot(X_grid, regressor.predict(X_grid), color = "blue")
plt.title('Truth of bluff( Regression Model)')
plt.xlabel('Position level ')
plt.ylabel('Salary')
plt.show()
