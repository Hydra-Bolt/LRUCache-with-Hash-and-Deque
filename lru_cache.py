from deque import Deque

class LRUCache:
    """
    An implementation of a Least Recently Used (LRU) Cache.
    """

    __miss = 0
    __hit = 0

    def __init__(self, capacity):
        """
        Initialize the LRUCache with a specified capacity.

        Args:
            capacity (int): The maximum number of key-value pairs the cache can hold.
        """
        assert (
            1 <= capacity <= 50
        ), "Capacity of cache can not be less than 1 and more than 50"
        self.capacity = capacity
        self.cache = {}
        self.order = Deque()

    def isFull(self):
        """
        Check if the cache is full.

        Returns:
            bool: True if the cache is full, False otherwise.
        """
        return self.order.size() >= self.capacity

    def get(self, key):
        """
        Get the value associated with the given key from the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            int: The value associated with the key, or -1 if the key is not in the cache.
        """
        if key in self.cache:
            # Move the key to the front to mark it as recently used
            self.order.items.remove(key)
            self.order.add_front(key)
            self.__hit += 1
            return self.cache[key]
        else:
            self.__miss += 1
            return -1

    def put(self, key, value):
        """
        Put a new key-value pair into the cache or update an existing one.

        Args:
            key: The key for the new or existing item.
            value: The value associated with the key.

        Raises:
            AssertionError: If key or value is out of size constraints.
        """
        assert 0 <= key <= 100, "Key Error: Out of size constraints"
        assert 0 <= value <= 100, "Value Error: Out of size constraints."
        
        if key in self.cache:
            # Update the value and move the key to the front
            self.cache[key] = value
            self.order.items.remove(key)
            self.order.add_front(key)
            self.__hit += 1
        else:
            if self.isFull():
                # Evict the least recently used key
                lru_key = self.order.remove_rear()
                del self.cache[lru_key]
            # Add the new key-value pair
            self.cache[key] = value
            self.order.add_front(key)
            self.__miss += 1

    def getMissRate(self):
        """
        Calculate the miss rate of the cache.

        Returns:
            float: The miss rate as a percentage. Ranges from 0-1
        """
        return self.__miss / (self.__hit + self.__miss)
    
    def __str__(self):
        """
        Return a string representation of the LRUCache.

        Returns:
            str: The string representation of the LRUCache.
        """
        cache_str = ", ".join(f"{key}: {self.cache[key]}" for key in self.order.items)
        return f"LRUCache({self.capacity}) -({cache_str})"
