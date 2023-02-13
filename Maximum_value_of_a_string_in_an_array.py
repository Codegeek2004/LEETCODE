class Solution(object):
    def maximumValue(self, s):
        k=[]
        for i in range(len(s)):
            if(s[i].isalpha()):
                p=len(s[i])
                k.append(p)
            elif(s[i].isdigit()):
                p=int(s[i])
                k.append(p)
            else:
                p=len(s[i])
                k.append(p)
        m=max(k)
        return m