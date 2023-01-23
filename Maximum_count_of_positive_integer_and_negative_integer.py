class Solution(object):
    def maximumCount(self, n):
        k=0
        l=0
        j=0
        for i in range(len(n)):
            if n[i]>0:
                k+=1
            elif n[i]==0:
                j+=1
            else:
                l+=1
        if l>k:
            return l
        else:
            return k
