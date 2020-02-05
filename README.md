# Maf Statistics

[![Total alerts](https://img.shields.io/lgtm/alerts/g/johnashu/Maffaz-Statistics-Calculations.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/johnashu/Maffaz-Statistics-Calculations/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/johnashu/Maffaz-Statistics-Calculations.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/johnashu/Maffaz-Statistics-Calculations/context:python)

A class that calculates averages such as mean, median etc, also to calculate stadard deviations, Variance and other statistical mathematical operations..

```python

ms = MafStats()

#ECDF
print("The ECDF of X is: \n", ms.ecdf(x), '\n')
print("The ECDF of Y is:\n", ms.ecdf(y), '\n')

#SQUAER ROOT
num_in = 25
print("The Square root of {} is:".format(num_in), ms.square_root(num_in))

#SUM OF ARRAY
return_sum_x = ms.sum(x)
print('\n\nThe Sum of X is:', return_sum_x)
return_sum_y = ms.sum(y)
print('The Sum of Y is:', return_sum_y)

#MEAN AVERAGE
mean_result_x = ms.mean(x)
print("The Mean Average of  X is:", mean_result_x)
print(np.mean(x))
mean_result_y = ms.mean(y)
print("The Mean Average of Y is:", mean_result_y)
print(np.mean(y))


#MEDIAN AVERAGE
median_res =  ms.median(x)
print("The Median of  X is:", median_res)
print(np.median(x))
median_res1 =  ms.median(y)
print("The Median of Y is:", median_res1)
print(np.median(y))

 # VARIANCE
var_result_x = ms.variance(x)
print("The Variance of  X is:", var_result_x)
var_result_y = ms.variance(y)
print("The Variance of Y is:", var_result_y)

# Standard Deviation
std_dev_x = ms.std_deviation(x)
print("The Standard Deviation Of Data  X is:", std_dev_x)
std_dev_y = ms.std_deviation(y)
print("The Standard Deviation Of Data Y is:", std_dev_y, '\n')

#calculate the Covariance of 2 arrays
covar_result = (ms.covariance(x, y))

print("The Covariance of X and Y is:", covar_result, '\n')

#standard correlation
#standard correlation

corr_result = ms.correlation(x, y)
print("The Correlation Coefficient between  X and Y is:", corr_result, '\n\n')

#Pearson Coefficient
print("The Pearson Correlation Coefficient is:", ms.pearson_correlation(x, y))

# Least Squares Regression
print("THe Least Square Regression Line Equation of X and Y is: ", ms.least_square_regression(x, y, 64))


# factorial
print(ms.factorial(2))

#Poisson distributoin
result = ms.poisson(5, 2)
print(result)


r_cul = ms.cul_poisson(5, 4)
print("Poisson Distribution is: ", r_cul)

# Test With Numpy functions.. 

import numpy as np

print("\nnumpy .cov function: \n", np.cov(x, y))
print("\nnumpy .corrcoef function: \n", np.corrcoef(x, y))
```
