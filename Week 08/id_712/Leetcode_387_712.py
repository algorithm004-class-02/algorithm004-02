# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 14:49:09 2019

@author: masha
"""
import string
class Solution:
    def firstUniqChar(self,s):
        letters=string.ascii_lowercase
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1