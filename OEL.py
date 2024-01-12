class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    missCount = 0
    hitCount = 0

    def __init__(self, capacity):
        assert 1 <= capacity <= 50, "Capacity should be greater than 1 and less than 50"
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        if key in self.cache:
            self.hitCount += 1
            node = self.cache[key]
            self.removeNode(node)
            self.addToHead(node)
            return node.value
        else:
            self.missCount += 1
            return -1

    def put(self, key, value):
        assert 0 <= key <= 100, "Key must be between 0 and 100"
        assert 0 <= value <= 100, "Value must be between 0 and 100"
        if key in self.cache:
            self.hitCount += 1
            node = self.cache[key]
            node.value = value
            self.removeNode(node)
            self.addToHead(node)
        else:
            if len(self.cache) == self.capacity:
                delKey = self.tail.prev.key
                del self.cache[delKey]
                self.removeNode(self.tail.prev)
            newNode = ListNode(key, value)
            self.cache[key] = newNode
            self.addToHead(newNode)
            self.missCount += 1

    def getMissRate(self):
        return self.missCount / (self.hitCount + self.missCount)

    def __str__(self):
        current = self.head.next
        cacheContent = []
        while current != self.tail:
            cacheContent.append((current.key, current.value))
            current = current.next
        cacheContent.reverse()
        cacheStr = f"LRUCache({self.capacity}): [\n"
        cacheStr += " <-> ".join([f"({key} = {value})" for key, value in cacheContent])
        cacheStr += "\n]"
        return cacheStr


# TEST CASE:
lruCache = LRUCache(50)

# Fill the cache using keys 0-49
for key in range(50):
    lruCache.put(key, key * 2)

# Retrieve the odd number key values
for key in range(1, 50, 2):
    print(f"Key: {key}, Value: {lruCache.get(key)}")

# Fill the cache with prime number keys 0-100
for key in range(2, 101):
    isPrime = all(key % i != 0 for i in range(2, int(key**0.5) + 1))
    if isPrime:
        lruCache.put(key, key / 2)

# Compute the final miss rate
missRate = lruCache.getMissRate()
print(f"Final Miss Rate: {missRate}")
print(lruCache)
