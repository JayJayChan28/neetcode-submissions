class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #two pointer technique
        #sort
        #end two pointer if l + r > target move r down, move left vide versa
        #edge cases: if duplicates in val we look at shift
        sorted_nums = sorted(nums)
        res = []

        for i, curr_val in enumerate(sorted_nums):
            if i > 0 and sorted_nums[i-1] == sorted_nums[i]:
                print(sorted_nums[i-1])
                print(sorted_nums[i])
                continue
            l = i + 1
            r = len(sorted_nums) - 1
            while l < r:
                if curr_val + sorted_nums[l] + sorted_nums[r] > 0:
                    r -= 1
                elif curr_val + sorted_nums[l] + sorted_nums[r] < 0:
                    l += 1
                else:
                    res.append([curr_val, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1  
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
        return res


