class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        res = float("-inf")
        l = 0 
        for r in range(len(s)):
            #adds to freq_map
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            #stores window len
            window_len = r - l + 1
            print(l)
            print(r)
            print(freq_map)
            print(freq_map.values())

            #calcs the num replacements 
            num_replace = window_len - max(freq_map.values())
            print(num_replace)
            #and only if # replacements less than k we update to get the max window len
            if num_replace <= k:
                res = max(res, window_len)
            #shift and remove window
            else:
                freq_map[s[l]] -= 1
                l += 1
        return res
            
