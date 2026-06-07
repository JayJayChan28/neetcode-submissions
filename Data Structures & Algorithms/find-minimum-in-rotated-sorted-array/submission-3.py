class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        mid = (l+r) // 2
        res = nums[mid] #set placeholder mid value as the minimum currently

        while l <= r:
            if nums[l] < nums[r]: # if we reach a soreted value
                res = min(res, nums[l])
                break
            elif nums[l] <= nums[mid]: # if we are in left portion
                l = mid + 1
            elif nums[r] > nums[mid]:
                r = mid - 1
            mid = (l + r) // 2
            res = min(res, nums[mid])
        return res



