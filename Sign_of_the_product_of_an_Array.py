class Solution(object):
    def arraySign(self, nums):
        m=1
        for i in nums:
            m=m*i
        if m<0:
            return -1
        elif m>0:
            return 1
        else:
            return 0