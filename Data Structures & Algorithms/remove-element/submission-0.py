class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        i = 0
        while i < k:
            if nums[i] == val:
                nums[i] = nums[k-1]
                k = k - 1
            else: 
                i = i + 1
        
        return k


