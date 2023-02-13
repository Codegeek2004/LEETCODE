class Solution(object):
    def singleNumber(self, n):
        k=0
        for i in n:
            k=k^i
        return k