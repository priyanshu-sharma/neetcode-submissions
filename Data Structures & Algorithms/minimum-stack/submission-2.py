class MinStack:

    def __init__(self):
        self.data = []
        self.total = 0
        self.gmini = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if self.total == 0:
            self.gmini.append(val)
        elif self.total > 0:
            self.gmini.append(min(val, self.gmini[-1]))
        self.total += 1

    def pop(self) -> None:
        if self.total > 0:
            self.data.pop(-1)
            self.gmini.pop(-1)
            self.total -= 1
        

    def top(self) -> int:
        return self.data[self.total - 1]
        

    def getMin(self) -> int:
        return self.gmini[self.total - 1]
        
