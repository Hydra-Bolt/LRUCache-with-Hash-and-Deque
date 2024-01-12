from lru_cache import LRUCache
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
print(f"Final Miss Rate: {missRate*100}%")