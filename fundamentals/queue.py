class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0 

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            # remove from first idx
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")
        
    def size(self):
        return len(self.items)

    def print(self):
        print("Queue:", self.items)



queue = Queue()
queue.print()

queue.enqueue(10)
queue.enqueue(20)
print(f'dequeue: {queue.dequeue()}')
queue.enqueue(30)
queue.enqueue(40)

queue.print()
print(f'peek: {queue.peek()}')
print(f'size: {queue.size()}')
print(f'empty: {queue.is_empty()}')
