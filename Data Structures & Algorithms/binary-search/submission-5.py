class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2

        while l < r:
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
            if nums[mid] == target:
                return mid
            mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        return -1