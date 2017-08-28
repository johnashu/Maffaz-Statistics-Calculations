data_array_x = [41,19,23,40,55,57,33]
data_array_y = [60,61,71,74,76,82,94]


#ecdf

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)
    # x-data for the ECDF: x
    x = np.sort(data)
    # y-data for the ECDF: y
    y = np.arange(1, n + 1) / n
    return x, y

#simple square root function
def maf_square_root(data):
    """ A function to calculate the Standard Deviation of Data 
    by caclulating the Square Root of The Variance"""
    var_sq = data ** (.5)
    return var_sq

# calculate the number of items int he array
def maf_sum(list):
    """ function that calculates the sum of an array"""           
    total_sum = 0
    for i in list:
        total_sum += i
    return float(total_sum)

return_sum_x = maf_sum(data_array_x)
print('\n\nThe Sum of X is:', return_sum_x)
return_sum_y = maf_sum(data_array_y)
print('The Sum of Y is:', return_sum_y)

#calculate the mean average
def maf_mean(array, sum_of_array):
    """ a function to calculate the mean average of an array"""
    n = float(len(array))
    mean_av = sum_of_array / n    
    return mean_av

mean_result_x = maf_mean(data_array_x, return_sum_x)
print("The Mean Average of  X is:", mean_result_x)
mean_result_y = maf_mean(data_array_y, return_sum_y)
print("The Mean Average of Y is:", mean_result_y)

# for fun calculate hte medain average
def maf_median(array):
    """ function that finds the median average of an array"""
    # https://www.mathsisfun.com/median.html   
    n = float(len(array))
    if n == n % 2:
        return n
    else:
        n += 1
        return n / 2 
   
median_res =  maf_median(data_array_x)
print("The Median of  X is:", median_res)
median_res1 =  maf_median(data_array_y)
print("The Median of Y is:", median_res1)

# calulate the variance
def maf_variance(array, mean_result):
    """ Function to calculate the Variance of data 
    by calculating the average of the squared differnces from the mean  """ 
    n = float(len(array))
    total_sum = 0
    for i in array:
        total_sum += ((mean_result - i) ** 2) / n
    return total_sum

var_result_x = maf_variance(data_array_x, mean_result_x)
print("The Variance of  X is:", var_result_x)
var_result_y = maf_variance(data_array_y, mean_result_y)
print("The Variance of Y is:", var_result_y)

#calculate standard deviation
def maf_std_deviation(var_result):
    """ A function to calculate the Standard Deviation of Data 
    by caclulating the Square Root of The Variance"""
    var_sq = var_result ** (.5)
    return var_sq

maf_std_dev_x = maf_std_deviation(var_result_x)
print("The Standard Deviation Of Data  X is:", maf_std_dev_x)
maf_std_dev_y = maf_std_deviation(var_result_y)
print("The Standard Deviation Of Data Y is:", maf_std_dev_y, '\n')

#calculate the Covariance of 2 arrays
def maf_covariance(array1, array2):
    """ function that calculates the Covariance  -
    Covariance measures how two variables move together. 
    It measures whether the two move in the same direction (a positive covariance) or 
    in opposite directions (a negative covariance).
    """
    assert float(len(array1)) == float(len(array2))
    n = float(len(array1))
    sum_array = 0

    for x, y in zip(array1, array2):
            sum_array += (x - mean_result_x) * (y - mean_result_y)

    total_sum = sum_array / (n - 1)

    return total_sum
    
covar_result = (maf_covariance(data_array_x, data_array_y))

print("The Covariance of X and Y is:", covar_result, '\n')

#standard correlation
def correlation(array1, array2):
    """ a function to determ,ine the correlation co-efficient between 2 sets of data """

    correlation = covar_result / (maf_std_dev_x * maf_std_dev_y)
    return correlation

corr_result = correlation(data_array_x, data_array_y)
print("The Correlation Coefficient between  X and Y is:", corr_result, '\n\n')

#Pearson Coefficient
def pearson_correlation(array1, array2):
    """Calculcates the Pearson Coefficient """
    n = len(array1)
    x_times_y = 0
    x_sq = 0
    y_sq = 0
    for i in range(n):
        x_min_mean = array1[i] - mean_result_x
        y_min_mean = array2[i] - mean_result_y
        x_times_y += x_min_mean * y_min_mean
        x_sq += x_min_mean ** 2
        y_sq += y_min_mean ** 2

    return x_times_y / maf_square_root(x_sq * y_sq)

print("The Pearson Correlation Coefficient is:", pearson_correlation(data_array_x, data_array_y))

# Test With Numpy functions.. 

import numpy as np

print("\nnumpy .cov function: \n", np.cov(data_array_x, data_array_y))
print("\nnumpy .corrcoef function: \n", np.corrcoef(data_array_x, data_array_y))
