

int findDuplicate(int* a, int numSize)
{
    int i,m=0,fm;
    for(i=0;i<numSize;i++)
    {
        if(a[i]>m)
        {
            m=a[i];
        }
    }
    int f[m+1];
    for(i=0;i<m+1;i++)
    {
        f[i]=0;
    }
    for(i=0;i<m+1;i++)
    {
        f[a[i]]++;
    }
    for(i=0;i<m+1;i++)
    {
        if(f[i]>1)
        {
            fm=i;
        }
    }
    return fm;

}