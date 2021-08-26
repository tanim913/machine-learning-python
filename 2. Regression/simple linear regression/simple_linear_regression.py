import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading dataset
dataset = pd.read_csv('Salary_Data.csv')

#distiguishing independent and dependant data
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 1].values

#splitting dataset into training set and test set 
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split (X,Y, test_size= 1/3,random_state = 0)

#fitting simple linear regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

#predicting the test sets result 
Y_pred = regressor.predict(X_test)
# Y_train_pred = regressor.predict(X_train)

#visualising training set result
plt.scatter(X_train, Y_train, color = 'purple')
plt.plot(X_train, regressor.predict(X_train),  color = 'brown')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience ')
plt.ylabel('Salary')
plt.show()

#visualising test set result
plt.scatter(X_test, Y_test, color = 'purple')
plt.plot(X_train, regressor.predict(X_train),  color = 'brown')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience ')
plt.ylabel('Salary')
plt.show()
