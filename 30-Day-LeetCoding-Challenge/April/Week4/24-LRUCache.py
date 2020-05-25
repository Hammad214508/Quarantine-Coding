"""
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least
recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.deque = deque()
        self.cache = {}

    # Returns the value associated with the key
    # It also updates the queue by removing the value for it and
    # adding it again tot the queue (most lecently used now)
    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            self._remove(key)
            self.deque.append((key,val))
            return val
        return -1

    # If key was already there then remove it from the queue
    # add it again as a mlu
    # add the k, v pair in the cache
    # if cache is full then delete the LRU value (head of queue)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(key)
        self.deque.append((key,value))
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            k, v = self.deque.popleft()
            del self.cache[k]

    # Removes k, v pair from tthe queue 
    def _remove(self, key):
        for k, v in self.deque:
                if k == key:
                    self.deque.remove((k, v))
                    break




capacity = 2
cache = LRUCache(capacity)
cache.put(2, 1)
cache.put(1, 1)
cache.put(2, 3)
cache.put(4, 1)
cache.get(1)
cache.get(2)
