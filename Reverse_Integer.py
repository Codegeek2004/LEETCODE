class Solution(object):
    def reverse(self, x):
        l=''
        if(x<0):
            l="-"
            s=abs(x)
            s=str(s)
            s=s[-1::-1]
            l=l+s
        else:
            s=str(x)
            s=s[-1::-1]
            l=l+s
        if(int(l) >= -2**31 and int(l) <= 2**31 - 1):
            return int(l)
        else:
            return 0