# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 23:34:39 2015

@author: Jordan Poles
"""
from math import floor
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
def binarySearch(arr, target):
    mini = 0;
    maxi = len(arr)-1
    while(maxi>=mini):
        guessindex = floor((mini+maxi)/2);
        guess=arr[guessindex]
        if guess==target:
            return guessindex;
        elif guess < target:
            mini = guessindex+1;
        elif guess > target:
            maxi = guessindex-1;
        else:
            raise ValueError("This shouldn't happen...");
            return -1;
    return -1;
print(binarySearch(primes, 61));