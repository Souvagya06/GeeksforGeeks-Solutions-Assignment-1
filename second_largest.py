class Solution:
    def getSecondLargest(self, arr):
        self.arr = arr
        m = list(set(self.arr))
        m.sort()
        if (len(m)==1):
            return -1
        elif (len(m)==0):
            return 0
        else:
            return m[-2]