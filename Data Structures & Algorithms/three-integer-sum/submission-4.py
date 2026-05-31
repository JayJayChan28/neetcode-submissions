class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
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
                else:
                    output.append([num, left_num, right_num])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # this part important to handle dublicates
                        l += 1

        return output
