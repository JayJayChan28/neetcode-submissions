class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #two pointer tech
        #check in left portion if target < leftmost serach right
        #if target > rightmost serach right otherwise serach left
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            #if the value is within the valid range
            #left portion
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                elif target < nums[l] or nums[mid] < target:
                    l = mid + 1
            #right portion
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                elif target < nums[mid] or nums[r] < target:
                    r = mid - 1

        return -1
            
