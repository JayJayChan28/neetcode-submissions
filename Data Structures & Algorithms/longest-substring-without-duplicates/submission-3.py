class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0 
        set_thing = set()
        max_total = 0
        while r <= len(s) - 1:
            if s[r] not in set_thing:
                set_thing.add(s[r])
                r += 1
            else:
                max_total = max(len(set_thing), max_total)
                set_thing = set()
                l += 1
                r = l
        if set_thing:
            max_total = max(len(set_thing), max_total)

        return max_total