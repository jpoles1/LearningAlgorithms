# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:30:41 2015

@author: Jordan Poles
"""
def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;
    return array;
def indexOfMinimum(array, startIndex):
    minValue = array[startIndex];
    minIndex = startIndex;
    for i in range(minIndex, len(array)):
        if(array[i] < minValue):
            minIndex = i;
            minValue = array[i];
    return minIndex;
def selectionSort(array):   
    for i in range(0, len(array)):
        smallest = indexOfMinimum(array, i);
        array = swap(array, i, smallest);
    return array;
def testing():
    assert swap([1,2,3], 0, 1) == [2,1,3]
    from numpy.random import randint
    runs = 1000;
    for i in range(runs):
        sortable = randint(1, 100, size=25).tolist();
        assert selectionSort(sortable) == sorted(sortable);