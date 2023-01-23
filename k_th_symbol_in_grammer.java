class Solution {
    public int kthGrammar(int n, int k) {
        if(k==1 || n==1) return 0;
        int numElements=(int)Math.pow(2,n-1-1);
        if(k<=numElements)
        {
            return kthGrammar(n-1,k);
        }
        else
        {
            return 1-kthGrammar(n-1,k-numElements);
        }
        
    }
}