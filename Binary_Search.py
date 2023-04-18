from itertools import islice
class Solution(object):
    def search(self, n, t):
        l= 0
        h= len(n)-1
        m=0
        while l<=h:
            m=(h+l)//2
            if n[m]<t:
                l=m+1
            elif n[m]>t:
                h=m-1
            else:
                return m
        return -1