class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = (len(nums1) + len(nums2)) // 2
        A, B = nums1, nums2

        #make A the smaller one
        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2 #left partition for A
            j = half - i - 2 #left partition for B
            left_A = A[i] if i >= 0 else float("-inf")#left index of A
            right_A = A[i + 1] if i + 1 < len(A) else float("inf") #right index of A
            left_B = B[j] if j >= 0 else float("-inf")#subtract two for 0 index
            right_B = B[j + 1] if j + 1 < len(B) else float("inf")
            if left_A <= right_B and left_B <= right_A:
                if total % 2 == 0:
                    return (min(right_B, right_A) + max(left_A, left_B))/2
                else:
                    return min(right_A, right_B)
            if left_A > right_B:
                r = i - 1
            else:
                l = i + 1
        
        


        
