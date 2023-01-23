class Solution(object):
    def capitalizeTitle(self, t):
        t=list(t.split(" "))
        for i in range(len(t)):
            if(len(t[i])==1 or len(t[i])==2):
                t[i]=t[i].lower()
            else:
                t[i]=t[i].lower()
                t[i]=t[i].capitalize()
        return " ".join(t)
        