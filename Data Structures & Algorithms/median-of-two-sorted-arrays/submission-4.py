class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        if len(A) > len(B):
            A, B = B, A
        half = (len(A) + len(B)) //2
        l, r = 0, len(A) - 1
        while True:
            mid = (l+r)//2
            B_mid = half - mid - 2
            A_left = A[mid] if mid >= 0 else float("-inf")
            B_left = B[B_mid] if B_mid >= 0 else float("-inf")
            A_right = A[mid + 1] if mid + 1 < len(A) else float("inf")
            B_right = B[B_mid + 1] if B_mid + 1 < len(B) else float("inf")
            if A_left > B_right:
                r = mid - 1
            elif B_left > A_right:
                l = mid + 1
            else:
                break
        if (len(A) + len(B)) % 2 == 0:
            return (min(A_right, B_right) + max(A_left, B_left)) / 2
        else:
            return min(B_right, A_right)









