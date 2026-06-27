class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        len_window = 0
        len_longest = float("-inf")
        l, r = 0, 0

        while r <= len(s) - 1:
            #counts frequency
            counter[s[r]] = counter.get(s[r], 0) + 1
            #if window is valid
            if (r - l + 1) - max(counter.values()) <= k:
                #update the longest length
                len_longest = max(len_longest, (r - l + 1))
                r += 1
            else:
                #deincrement value once it isnt in the window
                counter[s[l]] -= 1
                l += 1
                r += 1
        return len_longest