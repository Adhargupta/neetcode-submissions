class MinStack:

    def __init__(self):
        self.values = []

    def push(self, val: int) -> None:
        self.values = [val] + self.values

    def pop(self) -> None:
        self.values.pop(0)

    def top(self) -> int:
        return self.values[0]

    def getMin(self) -> int:
        return min(self.values)
        
