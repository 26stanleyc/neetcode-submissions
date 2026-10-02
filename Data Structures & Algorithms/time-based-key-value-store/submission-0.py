class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        i, j = 0, len(self.store[key])-1
        while(i<=j):
            mid = (i+j)//2
            if((mid == len(self.store[key]) - 1 or self.store[key][mid+1][1] > timestamp) and self.store[key][mid][1] <= timestamp):
                return self.store[key][mid][0]
            elif(timestamp < self.store[key][mid][1]):
                j = mid - 1
            else:
                i = mid + 1
        return ""
        
