class Solution(object):
    def permuteUnique(self, nums):
        self.nums=nums
        return (set(list(itertools.permutations(list(nums)))))
        