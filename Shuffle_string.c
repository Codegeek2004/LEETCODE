
char * restoreString(char * s, int* indices, int indicesSize){
char* res = (char*) malloc((indicesSize+1)*sizeof(char));

printf("%i", indicesSize - 1);
for(int i = 0; i < indicesSize; i++)
{
for(int j = 0; j < indicesSize; j++)
{
if(i == indices[j])
{
res[i] = s[j];
}
}
}

res[indicesSize] = '\0';

return res;
}



















