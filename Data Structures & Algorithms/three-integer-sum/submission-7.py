class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #two pointer
        #sort the values first
        #have one pointer on the first element, two poitner tecnique
        #sift left when our targets are < 0 vise versa for greater than 0 shift r
        #edge case #1 shfiting our reference pointer, if its same as the prev pointer skip
        #edge case #2, when we shift left, continue shifting left if the prev value is the same
        sorted_values = sorted(nums)
        res = []
        print(sorted_values)

        for i, curr in enumerate(sorted_values):
            l = i + 1
            r = len(nums) - 1
            #edge case 1 skip any duplicates
            if i > 0 and sorted_values[i] == sorted_values[i - 1]:
                continue
            while l < r:
                total = sorted_values[i] + sorted_values[l] + sorted_values[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                #when we reach a total that is valid
                else:
                    res.append([sorted_values[i], sorted_values[l], sorted_values[r]])
                    l += 1
                    r -= 1
                    while l < r and sorted_values[l] == sorted_values[l - 1]:
                        l += 1
        return res





            