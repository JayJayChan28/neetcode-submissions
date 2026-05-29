class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        #timestamp target, we want to find the most recent value less than the timestamp
        if len(self.hash_map[key]) < 1:
            return ""

        l = 0 #smallest time
        r = len(self.hash_map[key]) - 1 #longest time
        mid = (l + r) // 2
        res = ""

        print(self.hash_map[key])
        
        while l <= r: 
            if self.hash_map[key][mid][0] <= timestamp: #checks the lowerbound timestamp < target timestamp
                l = mid + 1
                res = self.hash_map[key][mid][1]
            elif self.hash_map[key][mid][0] > timestamp:
                r = mid - 1
            if self.hash_map[key][mid][0] == timestamp:
                return self.hash_map[key][mid][1]
            mid = (l + r)//2
        return res

        

