class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        list_key = self.hash_map[key]
        l = 0 # L index
        r = len(list_key) - 1 # right index
        mid = (l + r) // 2
        while l <= r:
            if list_key[mid][0] < timestamp:
                l = mid + 1
            elif list_key[mid][0] >= timestamp:
                r = mid - 1
            if list_key[mid][0] == timestamp:
                return list_key[mid][1]
            mid = (l + r) // 2
            print(r)
        if r < 0:
            return ""
        return list_key[r][1]

        
