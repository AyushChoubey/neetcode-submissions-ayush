
from collections import deque

class Node:
    def __init__(self,val = 0,key = 0,next = None, prev= None):

        self.val = val
        self.key = key
        self.next = next
        self.prev  = prev
        
class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.LRU = dict()
        self.head = Node(0,0,None,None)
        self.tail = Node(0,0,None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:

        if key in self.LRU:
            self.remove(self.LRU[key])
            self.insert(self.LRU[key])
            return self.LRU[key].val
        else:
            return -1


    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def insert(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.LRU:
            self.remove(self.LRU[key])
        self.LRU[key] = Node(value,key,None,None)
        self.insert(self.LRU[key])


        if len(self.LRU) > self.capacity:
            d = self.head.next
            self.remove(d)
            del self.LRU[d.key]

           
         

        
        
