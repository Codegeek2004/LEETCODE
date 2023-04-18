class Solution(object):
    def countOdds(self, l, h):
        
        if (l%2==0 and h%2==0):
            k=(h-l)//2
            return k
        elif (l%2!=0 and h%2!=0):
            k=(h-l)//2
            return k+1
        elif(l%2==0 and h%2!=0) or (l%2!=0 and h%2==0):
            k=((h-l)+1)//2
            return k
       