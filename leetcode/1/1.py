from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nDict = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nDict and nDict[complement] != i:
                return i, nDict[complement]