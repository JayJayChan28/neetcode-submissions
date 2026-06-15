class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #dynamic sliding window 
        #set!! for each value store in set
        #continue to increase window until we find dup, store len of window
        #then we decrease l pointer until all unique values exsist 
        unique_vals = set()
        l, r = 0, 0
        max_substring = 0
        while r <= len(s) - 1:
            if s[r] not in unique_vals:
                unique_vals.add(s[r])
                max_substring = max(max_substring, r - l + 1)
                r += 1
            else:
                unique_vals.remove(s[l])
                l += 1 



        return max_substring

            