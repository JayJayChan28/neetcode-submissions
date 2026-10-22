class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        have_count = 0 
        need_count = len(s1)
        index_map_s1  = [0] * 26
        index_map_s2 = [0] * 26

        if len(s1) > len(s2):
            return False
        #create the inde map of s1
        for val in s1:
            index = ord(val) - ord("a")
            index_map_s1[index] += 1
        l = 0
        for r in range(len(s2)):
            index_r = ord(s2[r]) - ord("a")
            #check the index of the right pointer to see if it exsists in our orginal index map --> we increment by one if true
            index_map_s2[index_r] += 1
            if  index_map_s2[index_r] <= index_map_s1[index_r]:
                have_count += 1
            
            #once we reach the window fixed size we remove the left end 
            if r > need_count - 1:
                index_l = ord(s2[l]) - ord("a")
                if index_map_s2[index_l] <= index_map_s1[index_l]:
                    have_count -= 1
                index_map_s2[index_l] -= 1
                l += 1
            if have_count == need_count:
                return True
        return False
            

                


            
                
        