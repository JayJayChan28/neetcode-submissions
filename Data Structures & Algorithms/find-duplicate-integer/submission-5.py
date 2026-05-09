class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f, s = 0, 0

        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        s1 = 0
        s2 = s

        while s1 != s2:
            s1 = nums[s1]
            s2 = nums[s2]


        return s1