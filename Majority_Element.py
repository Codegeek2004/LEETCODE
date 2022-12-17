class Solution(object):
    def majorityElement(self, n):
        d={}
        for i in n:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        return max(d,key=d.get)