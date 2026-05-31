class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i, num in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                left_num = nums[l]
                right_num = nums[r]
                target = num + left_num + right_num
                if target < 0:
                    l += 1
                elif target > 0:
                    r -= 1
                elif target == 0:
                    if [num, left_num, right_num] not in output:
                        output.append([num, left_num, right_num])
                    l += 1
        return output
