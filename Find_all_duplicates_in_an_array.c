

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDuplicates(int* a, int n, int* returnSize)
{
    int i, m=0,t=0;
    int *x= malloc(n*sizeof(int));
   
    for(i=0;i<n;i++)
    {
        if(m<a[i])
            m=a[i];
    }
    int f[m+1];
    for(i=0;i<m+1;i++)
    {
        f[i]=0;
    }
    for(i=0;i<n;i++)
    {
        f[a[i]]++;
    }
     
    for(i=0;i<m+1;i++)
    {
        if(f[i]>1)
        {
            x[t]=i;
            t++;
        }
    }
    *returnSize=t;
    return x;

}