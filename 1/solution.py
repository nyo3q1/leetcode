# https://leetcode.com/problems/two-sum/
import copy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _nums = copy.copy(nums)
        del _nums[0]
        for i, num in enumerate(nums):
            l = list(filter(lambda x: x + num == target, _nums))
            if len(l) > 0:
                return [i, _nums.index(l[0]) +i+1]
            del _nums[0]
