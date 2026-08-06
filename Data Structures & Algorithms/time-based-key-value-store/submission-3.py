class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.d:
            self.d[key] = []

        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.d:
            return ""

        ans = ""

        for t, value in self.d[key]:
            if t <= timestamp:
                ans = value
            else:
                break

        return ans
