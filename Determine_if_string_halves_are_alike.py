class Solution(object):
    def halvesAreAlike(self, s):
        self.s=s
        p=''
        o=''
        k=0
        l=0
        for i in range(len(s)/2):
            p=p+s[i]
        for i in range((len(s)/2),len(s)):
            o=o+s[i]
        for i in p:
            if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' 
               or i=='O' or i=='U'):
                k+=1
        for j in o:
            if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u' or j=='A' or j=='E' or j=='I' 
               or j=='O' or j=='U'):
                l+=1
        if(k==l):
            return 'true'
        
                
        