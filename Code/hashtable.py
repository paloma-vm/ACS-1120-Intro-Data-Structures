#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
        # TODO: Collect all values in each bucket
                all_values.append(value)
        return all_values
       

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        length = 0
        for bucket in self.buckets:
            for key, value in bucket.items():
        # TODO: Count number of key-value entries in each bucket
                length += 1
        return length

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        i = self._bucket_index(key)
        bucket = self.buckets[i] # help from Dani's Grain video
        entry = bucket.find_if_matches(lambda entry: entry[0] == key)
        
        # TODO: Check if key-value entry exists in bucket
        if entry is not None:
            return True
        else:
            return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        i = self._bucket_index(key)
        bucket = self.buckets[i] # help from Dani's Grain video
        entry = bucket.find_if_matches(lambda entry: entry[0] == key) # define matching function inline as a lamda function (anonymous function)
        # TODO: Check if key-value entry exists in bucket
        if entry is not None:
        # TODO: If found, return value associated with given key
            value = entry[1]
            return value
         
        # TODO: Otherwise, raise error to tell user get failed
        else:
            raise KeyError('Key not found: {}'.format(key))
        # Hint: raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        i = self._bucket_index(key)
        bucket = self.buckets[i] # help from Dani's Grain video
        entry = bucket.find_if_matches(lambda entry: entry[0] == key)
        # TODO: Check if key-value entry exists in bucket
        if entry is not None:
        # TODO: If found, update value associated with given key
            
            bucket.delete(entry)
            bucket.append((key, value)) # update by deleting the entry and adding updated entry
            return entry
        # TODO: Otherwise, insert given key-value entry into bucket
        else:
            bucket.append((key, value)) # append key:value as a tuple

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        i = self._bucket_index(key)
        bucket = self.buckets[i] # help from Dani's Grain video
        entry = bucket.find_if_matches(lambda entry: entry[0] == key)
        # TODO: Check if key-value entry exists in bucket
        if entry is not None:
        # TODO: If found, delete entry associated with given key
            # value = entry[1]
            bucket.delete(entry)
            # self.delete(bucket)
        # TODO: Otherwise, raise error to tell user delete failed
        else:
            raise KeyError('Key not found: {}'.format(key))
        # Hint: raise KeyError('Key not found: {}'.format(key))

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
