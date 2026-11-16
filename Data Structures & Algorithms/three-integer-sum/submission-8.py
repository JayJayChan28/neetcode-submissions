class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort aseneing
        #douple ened two pointer technique, 
        #no dublicates, so while next index still pointing to same value incremenet by i,  make sure pointer wihthin bounds

        nums.sort()
        res = []
        #note that the "target" is going to be 0

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = val + nums[r] + nums[l]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    while l < r and l + 1 <= len(nums) - 1 and nums[l] == nums[l+1]:
                        l += 1
                    res.append([val, nums[r], nums[l]])
                    l += 1
                    r -= 1
        return res