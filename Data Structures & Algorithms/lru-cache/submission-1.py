class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Remove from current position
        node.prev.next = node.next
        node.next.prev = node.prev

        # Move to front = MRU
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

        return node.value

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            # Remove from current position
            node.prev.next = node.next
            node.next.prev = node.prev

            # Move to MRU (after head)
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node

            return

        # Cache is full → remove LRU
        if len(self.cache) >= self.capacity:
            lru = self.tail.prev

            lru.prev.next = self.tail
            self.tail.prev = lru.prev

            del self.cache[lru.key]

        # Add new node as MRU
        new_node = Node(key, value)

        new_node.prev = self.head
        new_node.next = self.head.next

        self.head.next.prev = new_node
        self.head.next = new_node

        self.cache[key] = new_node
