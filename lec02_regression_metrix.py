# Module Name : lec02_regression_metrix.py
import numpy as np

#  MSE :
# RMSE :
# R^2  :

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

y_test = [4,2]
y_pred = [2,0]

y_test_mean = np.mean(y_test)
print("y_test_mean:" , y_test_mean)


# R^2 = 1 - SSE/SST
SST =  np.sum((y_test  - y_test_mean)**2)
# SSE  =  np.sum((y_test - t_pred)**2)
list = []
for i in range(2) :
    issr = (y_test[i] - y_pred[i]) **2
    list.append(issr)

SSE =  np.sum(list)

R2 = 1 - SSE/SST
print("R2:" , R2)  #-3.0

y_test = [2,0]
y_pred = [4,2]

mse =  mean_squared_error(y_test, y_pred, squared=True)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(mse , rmse , np.sqrt(mse))   #4.0 2.0


y_test = [2,0,4,5]
y_pred = [4,2,6,3]
y_test = np.array(y_test).reshape(-1,1)
y_pred = np.array(y_pred).reshape(-1,1)
from sklearn.linear_model import LinearRegression
lr_model = LinearRegression()
# sc = cross_val_score( scoring="neg_mean_squared_error")

# from sklearn import datasets, linear_model
# from sklearn.model_selection import cross_val_score
# diabetes = datasets.load_diabetes()
# X = diabetes.data[:150]
# y = diabetes.target[:150]
# lasso = linear_model.Lasso()
# print(cross_val_score(lasso, X, y, cv=3)) # [0.33150734 0.08022311 0.03531764]

from sklearn.model_selection import cross_val_score
neg_mse = cross_val_score(lr_model, y_test, y_pred,
                scoring="neg_mean_squared_error", cv=2)
print("neg_mse:" , neg_mse)   #[-160.   -8.]
print("mse:" , np.mean(neg_mse*-1))   #84.0

sklearn_api_mse = mean_squared_error(y_test, y_pred)
print("sklearn_api_mse:" , sklearn_api_mse)


# from sklearn.model_selection import GridSearchCV
# parm = {"max_dept":"10"}  #, param_grid=parm
# gcv = GridSearchCV(lr_model , scoring="neg_mean_squared_error", refit=True, cv=2)
# gcv.fit(X_trin, y_train)
# neg_mse = gcv.predict(X_test)
# print("MSE:" , np.mean(neg_mse*-1))







