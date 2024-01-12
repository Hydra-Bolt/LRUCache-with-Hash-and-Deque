class Deque:
    """
    A simple double-ended queue (deque) implementation.
    """

    def __init__(self):
        """
        Initialize an empty deque.
        """
        self.items = []

    def is_empty(self):
        """
        Check if the deque is empty.

        Returns:
            bool: True if the deque is empty, False otherwise.
        """
        return len(self.items) == 0

    def add_front(self, item):
        """
        Add an item to the front of the deque.

        Args:
            item: The item to be added to the deque.
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """
        Add an item to the rear of the deque.

        Args:
            item: The item to be added to the deque.
        """
        self.items.append(item)

    def remove_front(self):
        """
        Remove and return the item from the front of the deque.

        Returns:
            The item removed from the front of the deque.

        Raises:
            IndexError: If the deque is empty.
        """
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Deque is empty")

    def remove_rear(self):
        """
        Remove and return the item from the rear of the deque.

        Returns:
            The item removed from the rear of the deque.

        Raises:
            IndexError: If the deque is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Deque is empty")

    def size(self):
        """
        Get the current size of the deque.

        Returns:
            int: The size of the deque.
        """
        return len(self.items)

    def __str__(self):
        """
        Return a string representation of the deque.

        Returns:
            str: The string representation of the deque.
        """
        return str(self.items)
