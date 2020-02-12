# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        new_linked_pair = LinkedPair(key, value)

        index = self._hash_mod(key)

        if self.storage[index] is not None:
            if self.storage[index].key == key:
                self.storage[index] = new_linked_pair
                return
            current = self.storage[index]
            while current.next is not None: 
                if current.key == key:
                    current = new_linked_pair
                    break
                current = current.next
            current.next = new_linked_pair  
      
        else:
            self.storage[index] = new_linked_pair
        return


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            if self.storage[index].key == key:
                self.storage[index] = None
            else:
                current = self.storage[index]
                while current.next is not None: 
                    if current.key == key:
                        current = None
                        break
                    current = current.next


        else:
            print(f"Warning key ({key}) not found.")

        return


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            if self.storage[index].key == key:
                return self.storage[index].value
            else:
                current = self.storage[index]
                while current is not None: 
                    if current.key == key:
                        return current.value
                    current = current.next
        else:
            return None

        return


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for item in old_storage:
            if item is None: 
                pass
            elif item.next is None: 
                self.insert(item.key, item.value)
            else: 
                current = item
                while current is not None: 
                    self.insert(current.key, current.value)
                    current = current.next       



if __name__ == "__main__":
    #ht1 = HashTable(2)

    #ht1.insert("key1", "hello")
    #ht1.insert("unicorn", "goodbye")
    #ht1.remove("key1")

    #print(ht1.storage)

    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    # ht.insert("line_4", "Tiny hash table")
    # ht.insert("line_5", "Filled beyond capacity")
    # ht.insert("line_6", "Linked list saves the day!")
    # ht.insert("line_7", "Tiny hash table")
    # ht.insert("line_8", "Filled beyond capacity")
    # ht.insert("line_9", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    # print(ht.retrieve("line_4"))
    # print(ht.retrieve("line_5"))
    # print(ht.retrieve("line_6"))
    # print(ht.retrieve("line_7"))
    # print(ht.retrieve("line_8"))
    # print(ht.retrieve("line_9"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    # print(ht.retrieve("line_4"))
    # print(ht.retrieve("line_5"))
    # print(ht.retrieve("line_6"))
    # print(ht.retrieve("line_7"))
    # print(ht.retrieve("line_8"))
    # print(ht.retrieve("line_9"))

    print("")