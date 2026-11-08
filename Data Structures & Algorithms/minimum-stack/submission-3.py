class MinStack:

    def __init__(self):
        self.minStack = []
        self.mainStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)

        if not self.minStack or self.minStack[-1]>val:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.minStack.pop()
        return self.mainStack.pop()


    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return min(self.minStack)
        
