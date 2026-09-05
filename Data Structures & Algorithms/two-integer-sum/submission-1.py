class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lookup = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in lookup:
                return [nums.index(diff), i]
            lookup[n] = diff

        

