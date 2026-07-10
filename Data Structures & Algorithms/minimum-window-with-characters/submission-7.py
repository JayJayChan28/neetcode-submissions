class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have_mapping = {}
        need_mapping = Counter(t)
        have = 0
        need = len(need_mapping)
        min_len = float("inf")

        l, r = 0, 0
        if len(t) > len(s):
            return ""

        while r <= len(s) - 1:
            have_mapping[s[r]] = have_mapping.get(s[r], 0) + 1
            if s[r] in need_mapping and have_mapping[s[r]] == need_mapping[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < min_len:
                    min_indicies = (l, r)
                    min_len = r - l + 1
                have_mapping[s[l]] -= 1
                if s[l] in need_mapping and have_mapping[s[l]] < need_mapping[s[l]]:
                    have -= 1
                l += 1
            r += 1
        return s[min_indicies[0]: min_indicies[1] + 1] if min_len != float("inf") else ""
            

