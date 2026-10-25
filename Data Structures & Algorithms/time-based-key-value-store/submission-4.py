class TimeMap:

    def __init__(self):
        self.person_map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        #aceeses person and appends a new tuple of the (val, time)
        self.person_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        list_search = self.person_map[key]
        l, r = 0, len(self.person_map[key]) - 1

        while l <= r:
            mid_tuple = (l + r) // 2
            mid_time = list_search[mid_tuple][1]
            if mid_time == timestamp:
                return list_search[mid_tuple][0]
            if mid_time <= timestamp:
                l = mid_tuple + 1
            if mid_time > timestamp:
                r = mid_tuple - 1
        if r >= 0:
            return list_search[r][0]
        else:
            return ""


        
