# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 10:42:06 2019

@author: masha
"""
class Solution:
    def lengthOfLIS(self, nums):
        dp=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp[j])
        
