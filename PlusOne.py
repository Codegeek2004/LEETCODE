class Solution(object):
    def plusOne(self,d):
        h=[]
        s=""
        for i in d:
            s=s+str(i)
        s=str(int(s)+1)
        for i in s:
            h.append(int(i))
        return h
        