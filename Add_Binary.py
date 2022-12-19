class Solution(object):
    def addBinary(self, a, b):
        a=a[-1::-1]
        b=b[-1::-1]
        sa,sb=0,0
        j=0
        for i in range(len(a)):
            sa=sa+((int(a[i]))*(2**j))
            j+=1
        j=0
        for i in range(len(b)):
            sb=sb+((int(b[i]))*(2**j))
            j+=1
        s=sa+sb
        return str(bin(s))[2:]

    
        