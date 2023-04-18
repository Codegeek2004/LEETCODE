class Solution(object):
    def findTheDifference(self, s, t):
        d1={}
        d2={}
        for i in s:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for i in t:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
    
        for i in d2:
            if i not in d1:
                d1[i]=0
        l=""

        for i in d2:
            if(d2[i]>d1[i]):
                l+=str(i)
        
        return l        
            