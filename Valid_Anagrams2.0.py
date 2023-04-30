class Solution(object):
    def isAnagram(self, s, t):
        ds={}
        dt={}
        for i in s:
            if i in ds:
                ds[i]+=1
            else:
                ds[i]=1
        for i in t:
            if i in dt:
                dt[i]+=1
            else:
                dt[i]=1
        dsl=list(ds.values())
        dtl=list(dt.values())
        if(ds.keys()==dt.keys() and dsl==dtl):
            return True
        else:
            return False
