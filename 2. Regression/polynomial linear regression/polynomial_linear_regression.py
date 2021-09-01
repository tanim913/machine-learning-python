import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading dataset
dataset = pd.read_csv('Position_Salaries.csv')

#distiguishing independent and dependant data
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values

#fitting simple linear regression to the Training set
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, Y)

#fitting polynomial linear regression to the Training set
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
X_poly = poly_reg.fit_transform(X)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, Y)

#visualing the linear regreesion model
plt.scatter(X, Y, color = "red")
plt.plot(X, lin_reg.predict(X), color = "blue")
plt.title('Truth of bluff(linear regression)')
plt.xlabel('Position level ')
plt.ylabel('Salary')
plt.show()

#visualing the Polynomial regreesion model
#X_grid = np.arange(min(X), max(X), 0.1)
#X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, Y, color = "red")
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = "blue")
plt.title('Truth of bluff(Polynomial regression)')
plt.xlabel('Position level ')
plt.ylabel('Salary')
plt.show()

#predicting a new result with linear Regression
lin_reg.predict([[6.5]])

#predicting a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform(X))

