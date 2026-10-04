class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]: # left half is sorted
                if nums[l] <= target < nums[mid]: 
                    r = mid - 1 #target lies in sorted left half
                else: # lies in the messy right half
                    l = mid + 1
            else: 
                if nums[mid] < target <= nums[r]:
                    l = mid + 1 #target lies in sorted left half
                else:
                    r = mid - 1
        return -1