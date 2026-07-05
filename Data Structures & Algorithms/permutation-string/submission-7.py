class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = [0] * 26
        for i in range(len(s1)):
            encoding = ord(s1[i]) - ord('a')
            need[encoding] += 1
        have = [0] * 26
        print(need)
        l = 0
        for r in range(len(s2)):
            r_encoding = ord(s2[r]) - ord('a')
            have[r_encoding] += 1
            if r >= len(s1):
                l_encoding = ord(s2[l]) - ord('a')
                have[l_encoding] -= 1
                l += 1
            print(have)
            if need == have:
                return True
        return False
