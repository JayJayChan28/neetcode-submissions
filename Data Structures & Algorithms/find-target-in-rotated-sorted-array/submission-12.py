class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            #find mid calcualtions 
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid] and nums[l] <= target < nums[mid]:
                r = mid - 1
            elif nums[l] <= nums[mid] and not nums[l] < target < nums[mid]:
                l  = mid + 1
            elif nums[r] > nums[mid] and nums[mid] < target <= nums[r]:
                l = mid + 1
            elif nums[r] > nums[mid] and not nums[mid] < target < nums[r]:
                r = mid - 1
        return -1
        
            