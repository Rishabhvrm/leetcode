class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize

    # O(1)
    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    # O(1)
    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1
        
    # O(min(k, len of stack))
    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return
        
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)