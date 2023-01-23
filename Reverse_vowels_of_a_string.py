class Solution(object):
    def reverseVowels(self, s):
        f=[]
        for i in range(len(s)):
            if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
              f.append(s[i])

        g=f[-1::-1]
        s=list(s)
        for i in range(len(s)):
            if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
                s[i]=g[0]
                g.pop(0)
            
        s=''.join(s)
        return s   
                
        #g=''.join(g)
        
                
        

        