class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search Q's
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if nums[mid] == target:
                return mid

            #if left portion 
            if nums[l] <= nums[mid]:
                #check if we go to right portion
                if nums[l] <= target and nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            #now if its in right portion
            else:
                if nums[r] >= target and nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

                
                
            
                
            