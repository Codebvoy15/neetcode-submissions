class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

       if key not in self.store :
            self.store[key]=[] # just created a new list for teh key 
        
       self.store[key].append((value,timestamp))


    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""

        arr = self.store[key] # not clear about this 

        l = 0
        r = len(arr) - 1
        result = ""

        while l <= r:

            mid = (l + r) // 2

            if arr[mid][1] <= timestamp:
                result = arr[mid][0]
                l = mid + 1

            else:
                r = mid - 1

        return result
