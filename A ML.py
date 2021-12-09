

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

speed = [98, 89, 90, 91, 95, 101, 114, 76, 104, 98, 100]

x = np.mean(speed)                     # Will find the average speed
z = np.median(speed)                   # Will find the value in the middle
print(x)
print(z)


speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = stats.mode(speed)                   # Will find the most used speed
print(x)

# // Standard Deviation - square root of the variance //

speed = [86, 87, 88, 86, 87, 85, 86]

x = np.std(speed)                       # Find the average gap between
print(x)


speed = [32, 111, 138, 28, 59, 77, 97]

x = np.var(speed)                       # Will calculate the variance
print(x)                                # from value mean, difference from
# mean, averege number squared

# // 75 % of the list is 43 or younger //

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39,
        80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

x = np.percentile(ages, 75)

print(x)                                # Prints 43


# // 90 % of the list is younger than 61 //

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39,
        80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

x = np.percentile(ages, 90)

print(x)                                # Prints 61

# // Creates an array containing 250 floates from 0,0 -> 5,0 //

x = np.random.uniform(0.0, 5.0, 250)

print(x)


# // Draws a histogram of np.radom floats //

x = np.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)                          # Defines the histogram with 5 bars
plt.show()                              # Will show the histogram

# L.Value    H.Value     Size
# x = np.random.uniform(0.0, 5.0, 100000) #(low=0.0, high=5.0, size=100000)

# plt.hist(x, 100)                        # Defines the histogram with 100 bars
# plt.show()                              # Will show the histogram

# Mean/AVG     Deviation   Size
x = np.random.normal(5.0, 1.0, 100000)  # (loc=5.0, scale=1.0, size=100000)

plt.hist(x, 100)
plt.show()

# We use the array from the numpy.random.normal() method, with 100000 values,  to draw a histogram with 100 bars.
# We specify that the mean value is 5.0, and the standard deviation is 1.0.
# Meaning that the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.
# And as you can see from the histogram, most values are between 4.0 and 6.0, with a top at approximately 5.0.

# // Scatter Diagram - Dots placed randomly, in normal //

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]              # 13 Speeds
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]  # 13 Cars
# We assume that the x index macthes the y index
plt.scatter(x, y)
plt.show()
# The x-axis represents ages, and the y-axis represents speeds.
# What we can read from the diagram is that the two fastest cars were both 2 years old, and the slowest car was 12 years old.


x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y)
plt.show()
# We can see that the dots are concentrated around the value 5 on the x-axis, and 10 on the y-axis.
# We can also see that the spread is wider on the y-axis than on the x-axis.


# // Linear Regression - Can be used to predict future values //
# Find realationship between values

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]              # 13 Cars   / Array
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]  # 13 Speeds / Array

slope, intercept, r, p, std_err = stats.linregress(x, y)    # Method of line

# Create a function that uses the slope and intercept values to return a new value.
# This new value represents where on the y-axis the corresponding x value will be placed:


def myfunc(x):
    return slope * x + intercept


# Run each value of the x array through the function. This will result in a new array with new values for the y-axis:
mymodel = list(map(myfunc, x))

plt.scatter(x, y)       # Draw the original scatter plot:
plt.plot(x, mymodel)    # Draw the line of linear regression:
plt.show()              # Display the diagram:


#  R for Relationship
# It is important to know how the relationship between the values of the x-axis and the values of the y-axis is,
# if there are no relationship the linear regression can not be used to predict anything.

# This relationship - the coefficient of correlation - is called r.
# The r value ranges from -1 to 1, where 0 means no relationship, and 1 (and -1) means 100% related.
print(r)    # Value = -0,758591...


# // Predict Future Values //

# we try to predict the speed of a 10 year old car

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):
    return slope * x + intercept


speed = myfunc(10)
print(speed)        # Predicts that a 10yr old car will have the speed of 85.59

# https://www.w3schools.com/python/python_ml_polynomial_regression.asp
