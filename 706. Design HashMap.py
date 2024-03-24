class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        # initialize the bucket with dummy nodes,
        # choose a large prime for size of bucket
        self.map = [ListNode() for _ in range(2069)]

    def hash(self, key: int) -> int:
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        h = self.hash(key)
        curr = self.map[h]          # dummy node

        while curr.next:
            # update
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        
        # add new after last node
        curr.next = ListNode(key, value)


    def get(self, key: int) -> int:
        h = self.hash(key)
        curr = self.map[h]          # dummy node
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next

        return -1                   # key not found

    def remove(self, key: int) -> None:
        h = self.hash(key)
        curr = self.map[h]
        while curr:
            if curr.next.key == key:
                curr.next = curr.next.next      # del node
                return
            curr = curr.next

    def __repr__(self) -> str:
        return str(self.map)


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,10)
param_2 = obj.get(1)
print(param_2)
obj.remove(1)
param_3 = obj.get(1)
print(param_3)