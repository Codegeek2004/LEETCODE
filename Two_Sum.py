class Solution(object):
    def twoSum(self, n, t):
        self.n=n
        self.t=t
        k=[]
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if((n[i]+n[j])==t):
                    k.append(i)
                    k.append(j)
        return k
                    
        
        