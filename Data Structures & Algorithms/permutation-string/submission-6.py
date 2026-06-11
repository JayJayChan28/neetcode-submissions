class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq_map = [0] * 26 #input size doesnt increase as we iterate so we good O(1) space
        window_freq_map = [0] * 26
    
        #build freq_map for both for the fixed window
        for i in range(len(s1)):
            position1 = ord(s1[i]) - ord("a")
            position2 = ord(s2[i]) - ord("a")
            freq_map[position1] += 1
            window_freq_map[position2] += 1

        #fixed window length of size 0 - s1's length
        l, r = 0, len(s1) - 1
        while r < len(s2) - 1:
            if freq_map == window_freq_map:
                return True
            else:
                r += 1
                new_r_pos = ord(s2[r]) - ord("a")
                old_l_pos = ord(s2[l]) - ord("a")
                window_freq_map[old_l_pos] -= 1 # shoudl already exsist just remove
                l += 1 
                window_freq_map[new_r_pos] += 1 #add new map
            print(window_freq_map)
        return freq_map == window_freq_map # make sure to check last window's freq since we dont in the loop
