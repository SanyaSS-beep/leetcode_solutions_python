"""
@Description:
@Author: Mao Shuai Shuai
@Time: 2021/10/1 20:39
"""
from typing import List


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    real = nums[i] + nums[j]
                    if real == target:
                        return [i, j]
                        break


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [i, hashtable[target-num]]
            else:
                hashtable[nums[i]] = i
        return []