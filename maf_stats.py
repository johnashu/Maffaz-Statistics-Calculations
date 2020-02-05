x = [41,19,23,40,55,57,33]
y = [60,61,71,78,76,82,945]

import numpy as np

class MafStats:
    
    #ecdf
    def ecdf(self, data):
        """Compute ECDF for a one-dimensional array of measurements."""
        # Number of data points: n
        n = len(data)
        # x-data for the ECDF: x
        x = np.sort(data)
        # y-data for the ECDF: y
        y = np.arange(1, n + 1) / n
        return x, y
        
    #simple square root function
    def square_root(self, data):
        """ A function to calculate the Standard Deviation of Data 
        by caclulating the Square Root of The Variance"""
        var_sq = data ** (.5)
        return var_sq
        
    # calculate the number of items int he array
    def sum(self, list):
        """ function that calculates the sum of an array"""           
        total_sum = 0
        for i in list:
            total_sum += i
        return float(total_sum)
        
    #calculate the mean average
    def mean(self, array):
        """ a function to calculate the mean average of an array"""
        n = float(len(array))
        mean_av = self.sum(array) / n    
        return mean_av
        
    # for fun calculate hte medain average
    def median(self, array):
        """ function that finds the median average of an array"""
        # https://www.mathsisfun.com/median.html   
        n = len(array)
        if n < 1:
                return None
        if n % 2 == 1:
            # for an odd array, return the middle number
                return sorted(array)[n // 2]
        else:
                return float(sum(sorted(array)[self.mean(array)]) / 2.0)
            
    # calulate the variance
    def variance(self, array):
        """ Function to calculate the Variance of data 
        by calculating the average of the squared differnces from the mean  """ 
        n = float(len(array))
        total_sum = 0
        for i in array:
            total_sum += ((self.mean(array) - i) ** 2) / n
        return total_sum
        
    #calculate standard deviation
    def std_deviation(self, array):
        """ A function to calculate the Standard Deviation of Data 
        by caclulating the Square Root of The Variance"""
        var_sq = self.variance(array) ** (.5)
        return var_sq
        
    #calculate the Covariance of 2 arrays
    def covariance(self, array1, array2):
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
    
    #correlation co-efficient    
    def correlation(self, array1, array2):
        """ a function to determ,ine the correlation co-efficient between 2 sets of data """
    
        correlation = covar_result / (std_dev_x * std_dev_y)
        return correlation
    
    #Pearson Coefficient    
    def pearson_correlation(self, array1, array2):
        """Calculcates the Pearson Coefficient """
        n = len(array1)
        x_times_y = 0
        x_sq = 0
        y_sq = 0
        for i in range(n):
            x_min_mean = array1[i] - self.mean(array1)
            y_min_mean = array2[i] - self.mean(array2)
            x_times_y += x_min_mean * y_min_mean
            x_sq += x_min_mean ** 2
            y_sq += y_min_mean ** 2
    
        return x_times_y / self.square_root(x_sq * y_sq)
        
    # Least square regression
    def least_square_regression(self, x, y, var):
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

    # factorial
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)
            
    def poisson(self, events, interval):
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
    
        x1 = self.factorial(x)
              
        #The Poisson probability that exactly x successes occur in a Poisson experiment, when the mean number of successes is μ. 
        p = ((e ** -u) * (u ** x)) / x1
    
        return p
        
    def cul_poisson(self, events, list):
        """
        In probability theory, the Poisson distribution is a very common discrete probability distribution.  A Poisson distribution helps in describing the chances of occurrence of a number of events in some given time interval or given space conditionally that the value of average number of occurrence of the event is known. This is a major and only condition of Poisson distribution.
    
        1. The experiment results in outcomes that can be classified as successes or failures.
        2. The average number of successes (μ) that occurs in a specified region is known.
        3. The probability that a success will occur is proportional to the size of the region.
        4. The probability that a success will occur in an extremely small region is virtually zero.
    
        """
    
        # The mean number of successes that occur in a specified region.
        uc = events
    
        # A list of the actual number of successes that occur in a specified region
        xl = range(list)
    
        cul = 0
    
        for i in xl:
            r = self.poisson(uc, i)
            cul += r
    
        pc = cul
        
        return pc

