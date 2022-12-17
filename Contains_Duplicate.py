import collections
class Solution(object):
    def containsDuplicate(self, n):
        d=dict(collections.Counter(n))
        for i in d:
            if(d[i]>=2):
                return True
                break
        return False