class DLLNode(object):
    """
    Double Linked List Node to keep the key and value of the entry
    in the cache memory.
    """
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None

    def __str__(self):
        return "(%s, %s)" % (self.key, self.value)



class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        if capacity < 1:
            print ("cache reached it's capacity")
            
        self.capacity = capacity
        self._size = 0 
        self._nodes = {}
        self._head = None  
        self._tail = None  
        

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self._nodes:
            node = self._nodes[key]

            # update pointers only if this is not head; otherwise return
            if self.head != node:
                self._remove(node)
                self._set_head(node)

            return node.value

        return -1

        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self._nodes:
            node = self._nodes[key]
            node.value = value

            # update pointers 
            if self.head != node:
                self._remove(node)
                self._set_head(node)
        else:
            new_node = DLLNode(key, value)
            if self._size == self.capacity:
                del self._nodes[self.tail.key]
                self._remove(self.tail)
                self._size -= 1
            self._set_head(new_node)
            self._nodes[key] = new_node
            self._size += 1
  
        pass



    def display(self):
        n = self.head
        print("[head = %s, tail = %s]" % (self.head, self.tail), end=" ")
        while n:
            print("%s -> " % (n), end = "")
            n = n.next
        print("NULL")


    def _set_head(self, node):
        if self._size == 0:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node


    def _remove(self, node):

        if self._size == 0:
            return None

        if self._size == 1:
            self.head = None
            self.tail = None
        elif self.tail == node:
            node.prev.next = None
            self.tail = node.prev
            node.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = None
            node.prev = None
            node.next = None

        return node

    
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print('our_cache.set(1,1); our_cache.set(2,2); our_cache.set(3,3); our_cache.set(4,4)')

our_cache.display()

# retrieve values 
print('our_cache.get(1): {}'.format(our_cache.get(1)))  # returns 1
our_cache.display()
print('our_cache.get(2): {}'.format(our_cache.get(2)))  # returns 1
our_cache.display()

print('our_cache.get(9): {}'.format(our_cache.get(9)))  # returns -1



print('our_cache.set(5,5); our_cache.set(6,6)')

our_cache.set(5, 5)
our_cache.set(6, 6)
our_cache.display()

print('our_cache.get(3): {}'.format(our_cache.get(3)))  # returns -1

# overwrite an existing key
our_cache.set(2, 5);
print('our_cache.set(3,5)')

our_cache.display()

# Capacity < 1
our_cache2 = LRU_Cache(-1)

