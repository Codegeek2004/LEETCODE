import collections
class Solution(object):
    def singleNumber(self, nums):
        self.nums=nums
        l=collections.Counter(nums)
        for i in l:
            if(l[i]==1):
                k=i
        return k
        