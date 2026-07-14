class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        res = float("-inf")
        max_freq = 0
        l = 0 
        for r in range(len(s)):
            #adds to freq_map
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            if freq_map[s[r]] > max_freq:
                max_freq = freq_map[s[r]]
            #stores window len
            window_len = r - l + 1

            #calcs the num replacements 
            num_replace = window_len - max_freq
            #and only if # replacements less than k we update to get the max window len
            if num_replace <= k:
                res = max(res, window_len)
            #shift and remove window
            else:
                freq_map[s[l]] -= 1
                l += 1
        return res
            
