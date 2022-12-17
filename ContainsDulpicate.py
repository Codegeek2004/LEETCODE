class Solution(object):
    def containsDuplicate(self, n):
        d={}
        for i in n:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        print(d)
        for i in d:
            if(d[i]>=2):
                return True
                break
        return False
                