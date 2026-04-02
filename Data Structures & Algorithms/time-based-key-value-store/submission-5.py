class TimeMap:

    def __init__(self):
       self.dict_ = {}

    def search_timestamp(self, key, timestamp):
        if key not in self.dict_:
            return ""

        l = 0
        r = len(self.dict_[key]) - 1
        res = ""

        while l <= r:
            m = l + (r - l) // 2

            if self.dict_[key][m][1] < timestamp:
                res = self.dict_[key][m][0]
                l = m + 1

            elif self.dict_[key][m][1] > timestamp:
                r = m - 1

            else:
                return self.dict_[key][m][0]

        return res

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict_:
            self.dict_[key] = []
        self.dict_[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        return self.search_timestamp(key, timestamp)