"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        count = 0
        for ele in arr:
            if ele == x:
                count += 1
        return count