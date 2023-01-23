import itertools
class Solution(object):
    def permute(self, nums):
        self.nums=nums
        return list(itertools.permutations(list(nums)))