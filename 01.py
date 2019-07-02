"""
 Create by zipee on 2019/7/2.
"""
__author__ = 'zipee'


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            left = target - num
            if left in d:
                return [d[left], i]
            d[num] = i
        return []