x = [41,19,23,40,55,57,33]
y = [60,61,71,74,76,82,94]



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

return_sum_x = maf_sum(x)
print('\n\nThe Sum of X is:', return_sum_x)
return_sum_y = maf_sum(y)
print('The Sum of Y is:', return_sum_y)

#calculate the mean average
def maf_mean(array, sum_of_array):
    """ a function to calculate the mean average of an array"""
    n = float(len(array))
    mean_av = sum_of_array / n    
    return mean_av

mean_result_x = maf_mean(x, return_sum_x)
print("The Mean Average of  X is:", mean_result_x)
mean_result_y = maf_mean(y, return_sum_y)
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
   
median_res =  maf_median(x)
print("The Median of  X is:", median_res)
median_res1 =  maf_median(y)
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

var_result_x = maf_variance(x, mean_result_x)
print("The Variance of  X is:", var_result_x)
var_result_y = maf_variance(y, mean_result_y)
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

    for (x, y) in zip(array1, array2):
            sum_array += (x - mean_result_x) * (y - mean_result_y)

    total_sum = sum_array / (n - 1)

    return total_sum
    
covar_result = (maf_covariance(x, y))

print("The Covariance of X and Y is:", covar_result, '\n')

#standard correlation
def correlation(array1, array2):
    """ a function to determ,ine the correlation co-efficient between 2 sets of data """

    correlation = covar_result / (maf_std_dev_x * maf_std_dev_y)
    return correlation

corr_result = correlation(x, y)
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

print("The Pearson Correlation Coefficient is:", pearson_correlation(x, y))

def maf_least_square_regression(x, y, var):
    """ 
    Least square regression is a method for finding a line that summarizes the relationship between the two variables, at least within the domain of the explanatory variable x.
    calculate the least square regression line equation with the given x and y values. 
    """
    # Count the number of given x values. 
    n = len(x)

    #Find XY, X2 for the given values.
    def xy_x2(x, y):
        
        xx = [i ** 2 for i, j in zip(x, y)]
        xy = [i * j for i, j in zip(x, y)]
        return xx, xy

    xx, xy = xy_x2(x, y)
    
    #Find ∑X, ∑Y, ∑XY, ∑X2 for the values
    ex = sum(x)
    ey = sum(y)
    exy = sum(xy)
    ex2 = sum(xx)

   # Slope Formula
    # Slope(b) = (N∑XY - (∑X)(∑Y)) / (N∑X2 - (∑X)2)
    b = ((n) * (exy) - (ex) * (ey)) / ((n) * (ex2) - (ex) ** 2) 

    # intercept formula
    # Intercept(a) = (∑Y - b(∑X)) / N 
    a = (ey - b * ex) / n 

    # Regression Equation(y) = a + bx 
    reg_eq = a + (b * var)
    
    return reg_eq

print("THe Least Square Regression Line Equation of X and Y is: ", maf_least_square_regression(x, y, 64))

def maf_factorial(n):
    if n == 0:
        return 1
    else:
        return n * maf_factorial(n-1)
print(maf_factorial(0))

def maf_poisson(events, interval):
    """
    In probability theory, the Poisson distribution is a very common discrete probability distribution.  A Poisson distribution helps in describing the chances of occurrence of a number of events in some given time interval or given space conditionally that the value of average number of occurrence of the event is known. This is a major and only condition of Poisson distribution.

    1. The experiment results in outcomes that can be classified as successes or failures.
    2. The average number of successes (μ) that occurs in a specified region is known.
    3. The probability that a success will occur is proportional to the size of the region.
    4. The probability that a success will occur in an extremely small region is virtually zero.

    """
    # base value of the system of natural logarithm
    e = 2.71828459

    # The mean number of successes - Average Rate of Success.
    u = events

    # The actual number of successes that occur - Poisson Random Variable
    x = interval

    x1 = maf_factorial(x)
          
    #The Poisson probability that exactly x successes occur in a Poisson experiment, when the mean number of successes is μ. 
    p = ((e ** -u) * (u ** x)) / x1

    return p
    
result = maf_poisson(5, 2)

def maf_cul_poisson(events, list):
    """
    In probability theory, the Poisson distribution is a very common discrete probability distribution.  A Poisson distribution helps in describing the chances of occurrence of a number of events in some given time interval or given space conditionally that the value of average number of occurrence of the event is known. This is a major and only condition of Poisson distribution.

    1. The experiment results in outcomes that can be classified as successes or failures.
    2. The average number of successes (μ) that occurs in a specified region is known.
    3. The probability that a success will occur is proportional to the size of the region.
    4. The probability that a success will occur in an extremely small region is virtually zero.

    """
    # base value of the system of natural logarithm
    e = 2.71828459

    # The mean number of successes that occur in a specified region.
    uc = events

    # A list of the actual number of successes that occur in a specified region
    xl = range(list)

    cul = 0

    for i in xl:
        r = maf_poisson(uc, i)
        cul += r

    pc = cul
    
    return pc

r_cul = maf_cul_poisson(5, 4)




# Test With Numpy functions.. 

import numpy as np

print("\nnumpy .cov function: \n", np.cov(x, y))
print("\nnumpy .corrcoef function: \n", np.corrcoef(x, y))



