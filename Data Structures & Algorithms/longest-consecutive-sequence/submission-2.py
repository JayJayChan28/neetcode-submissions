class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()

        for val in nums:
            hash_set.add(val)
        print(hash_set)
        
        max_len = 0
        for val in nums:
            if val - 1 in hash_set:
                continue
            curr_len = 0
            start_sequence = val
            while start_sequence in hash_set:
                curr_len += 1
                start_sequence += 1
            #sets the max length of each "sucessesful" start to a sequence
            max_len = max(max_len, curr_len)
        return max_len

                


