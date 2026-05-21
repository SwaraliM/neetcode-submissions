class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productOfAllNums, zero_count = 1, 0
        for num in nums:
            if num:
                productOfAllNums *= num
            else:
                zero_count += 1
            if zero_count > 1: return[0] * len(nums)
            
        output = [0] * len(nums) 
        for i, num in enumerate(nums):
            if zero_count: 
                output[i] = 0 if num else productOfAllNums
            else: 
                output[i] = productOfAllNums // num
        return output