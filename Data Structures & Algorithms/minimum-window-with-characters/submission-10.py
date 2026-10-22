class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #create a have & need
        have_count = 0 
        need_count = len(t)

        have_map = {}
        need_map = Counter(t)
        #dont know the way for fixed array size, so will just use hash_map for now
        min_len = float("inf")
        min_str = ""

        l = 0
        #lets increment the r pointer
        for r in range(len(s)):
            #now we insert the val into the have_map
            have_map[s[r]] = have_map.get(s[r], 0) + 1
            if have_map[s[r]] <= need_map.get(s[r], 0):
                have_count += 1

            while need_count == have_count:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    best_l = l
                have_map[s[l]] -= 1
                if have_map[s[l]] < need_map[s[l]]:
                    have_count -= 1
                l += 1
        return s[best_l : best_l + min_len] if min_len != float("inf") else ""























