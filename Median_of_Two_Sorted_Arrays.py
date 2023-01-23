class Solution(object):
    def findMedianSortedArrays(self, n1,n2):
        s=n1+n2
        s=sorted(s)
        k=len(s)
        if(k%2)!=0:
            t=("%.5f" % (s[k/2]))
        else:
            t=("%.5f" % ((s[(k//2)-1]+(s[(k//2)]))/2.0))
        return float(t)


