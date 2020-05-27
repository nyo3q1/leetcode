# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
from copy import copy
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [self.isMax(candies, extraCandies, i) for i, v in enumerate(candies)]
        
    def isMax(self, cs, ex, i):
        _cs = copy(cs)
        _cs[i] = _cs[i] + ex
        return max(_cs) == cs[i] + ex
