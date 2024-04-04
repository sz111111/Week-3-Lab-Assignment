# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 04:39:43 2024

@author: ChelseySSS
"""

#SHIHAN ZHAO
#As always, attempt your lab without searching for solutions online unless otherwise noted

#1: This code does not run!  Try it and examine the errors, then figure out what needs to
#be changed to make it work.  Do not create any, global variables, delete any existing
#code, or cut and paste existing code to new locations.


a = 10

def first_func(b=20):
    c = 30
    # Pass b and c as arguments to second_func
    value = second_func(b, c)
    return value

# Adjust second_func to accept b and c as parameters
def second_func(b, c, d=40):
    e = 50
    return a + b + c + d + e

result = first_func()


#2: Take this code from last week's lab and write functions so that the final
#execution looks like:
#answer = {key_func(k):val_func(v) for k, v in start_dict.items()}

#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}


import datetime
start_dict = {
    'noah': '2/23/1999',
    'sarah': '9/1/2001',
    'zach': '8/8/2005'
}

def key_func(k):
    # Capitalize the first letter of the key
    return k.capitalize()

def val_func(v):
    # Convert the string date to a datetime object
    return datetime.datetime.strptime(v, '%m/%d/%Y')

# Using dictionary comprehension to transform start_dict
answer = {key_func(k): val_func(v) for k, v in start_dict.items()}

print(answer)


#3: A zscore is one term to describe data transformed to have mean zero and
#standard deviation one, given by: x - x_mean / x_std
#Write a function that takes any list-like object as a positional argument,
#then returns an object of the same dimensions with the zscores for the series.
#Use these two imported functions, and test your results on several lists of
#values

from numpy import mean, std

def calculate_zscores(values):
    values_mean = mean(values)
    values_std = std(values)
    zscores = [(x - values_mean) / values_std for x in values]
    return zscores

# Testing the function with several lists of values
list1 = [1, 2, 3, 4, 5]
list2 = [30, 40, 50, 60, 70]
list3 = [-5, 0, 5, 10, 15]

# Calculate z-scores for each list
z_scores_list1 = calculate_zscores(list1)
z_scores_list2 = calculate_zscores(list2)
z_scores_list3 = calculate_zscores(list3)

print(z_scores_list1, z_scores_list2, z_scores_list3)


#4: A modified zscore uses the "median absolute deviation" to better handle
#outliers in the data, where the MAD is calculated by:
#  1. x - the median of the series
#  2. the absolute values of the results from 1
#  3. the median of the results from 2
#and finally, replace the standard deviation in the formula for the zscore from
#question 3 with the results from this process: x - x_mean / MAD
#
#Copy the function you created in 3 and create an optional key word argument that
#lets you override the default zscore calculation to instead use the modified
#version. This function should work in both question 3 and 4 without needing to
#change how you call it in part 3, because of its default behavior

from numpy import mean, std, median, absolute

def calculate_zscores(values, use_modified=False):
    if use_modified:
        # Calculate the Median Absolute Deviation (MAD)
        med = median(values)
        mad = median(absolute(values - med))
        # Avoid division by zero; if mad is 0, add a small value (epsilon)
        if mad == 0:
            mad += 1e-6
        zscores = [(x - mean(values)) / mad for x in values] 
    else:
        # Standard z-score calculation
        values_mean = mean(values)
        values_std = std(values)
        zscores = [(x - values_mean) / values_std for x in values]
    return zscores

# Testing the function I created in #3
list1 = [1, 2, 3, 4, 5]
list2 = [30, 40, 50, 60, 70]
list3 = [-5, 0, 5, 10, 15]

# Testing the function for standard z-score calculation
z_scores_list1 = calculate_zscores(list1)
z_scores_list2 = calculate_zscores(list2)
z_scores_list3 = calculate_zscores(list3)

# Testing the function for modified z-score calculation
modified_z_scores_list1 = calculate_zscores(list1, use_modified=True)
modified_z_scores_list2 = calculate_zscores(list2, use_modified=True)
modified_z_scores_list3 = calculate_zscores(list3, use_modified=True)

print(z_scores_list1, z_scores_list2, z_scores_list3)
print(modified_z_scores_list1, modified_z_scores_list2, modified_z_scores_list3)














