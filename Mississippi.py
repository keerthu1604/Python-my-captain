# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 15:11:50 2021

@author: keekee
"""

a= input('Please enter a string ')
def most_frequent(string):
    d = dict();
    for i in string:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

print (most_frequent(a))