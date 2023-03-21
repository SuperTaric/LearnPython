class DLinkedNode:
    def __init__(self, key=0, value=0) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value
    
    def put(self, key: int, value: int):
        if key not in self.cache:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node: DLinkedNode):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node: DLinkedNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node: DLinkedNode):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
    
if __name__ == '__main__':
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1) # 缓存是 {1=1}
    lRUCache.put(2, 2) # 缓存是 {1=1, 2=2}
    print(lRUCache.get(1))    # 返回 1
    lRUCache.put(3, 3) # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    print(lRUCache.get(2))   # 返回 -1 (未找到)
    lRUCache.put(4, 4) # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    print(lRUCache.get(1))   # 返回 -1 (未找到)
    print(lRUCache.get(3))    # 返回 3
    print(lRUCache.get(4))   # 返回 4
    print(lRUCache)