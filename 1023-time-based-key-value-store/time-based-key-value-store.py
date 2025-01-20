class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""
        
        valList = self.hashMap[key]
        
        # Binary search to find the largest timestamp <= the requested timestamp
        left, right = 0, len(valList) - 1
        
        if not valList or valList[0][0] > timestamp:
            return ""
        
        while left < right:
            mid = (left + right + 1) // 2  # Correct midpoint calculation
            if valList[mid][0] <= timestamp:
                left = mid  # Move left boundary to mid if mid timestamp is valid
            else:
                right = mid - 1  # Otherwise, shrink the search range

        # After the loop, left should point to the closest timestamp <= the requested timestamp
        return valList[left][1] if valList[left][0] <= timestamp else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)