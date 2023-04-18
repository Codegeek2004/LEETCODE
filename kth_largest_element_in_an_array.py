import heapq
class Solution(object):
    def findKthLargest(self, n, k):
        l=[]
        for i in range(k):
            l.append(n[i])
        heapq.heapify(l)
        for i in range(k,len(n)):
            if(n[i]>l[0]):
                heappop(l)
                heappush(l,n[i])
        return l[0]


            

            






        