class Solution(object):
    def findTheArrayConcVal(self, n):
        c=0
        if(len(n)%2==0):
            while(len(n)!=0):
                f=str(n[0])+str(n[-1])
                c=c+int(f)
                n.pop()
                n=n[1:]
        else:
            m=n[len(n)//2]
            c=c+m
            t=n[:len(n)//2]+n[(len(n)//2)+1:]
            while(len(t)>0):
                f=str(t[0])+str(t[-1])
                c=c+int(f)
                t.pop()
                t=t[1:]
        return c

            