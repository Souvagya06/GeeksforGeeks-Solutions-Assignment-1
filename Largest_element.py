class Solution:
    def largest(self, arr):
        self.arr = arr
        m = list(set(self.arr))
        m.sort()
        return m[-1]
        
