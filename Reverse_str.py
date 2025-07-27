class Solution:
    def reverseString(self, s: str) -> str:
        l = []
        for ele in s:
            l.append(ele)
        l.reverse()
        m = ''.join(l)
        return m