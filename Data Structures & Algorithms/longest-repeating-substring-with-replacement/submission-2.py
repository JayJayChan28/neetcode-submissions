class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        l = 0
        max_window = 0

        for r in range(len(s)):
            len_window = r - l + 1
            hash_map[s[r]] = hash_map.get(s[r], 0) + 1
            num_replaces = len_window - max(hash_map.values()) 
            if num_replaces > k:
                hash_map[s[l]] -= 1 #deincrement l pointer
                l += 1
            else:
                valid_window = r - l + 1
                max_window = max(max_window, valid_window)

            
        return max_window
            
