#!python
# I had code that was up to the point of 5 fail, 12 pass.
# prepend and delete were not working well, so I changed to what
# Dani showed us in class.  I left some of my old code on the page for 
# reference.

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        node = self.head
        n = 0
        while node is not None:
            n += 1
            node = node.next
        return n

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        node =  Node(item)
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        if self.is_empty():
            self.head = node
            self.tail = node
            self.size = 1
            
        # TODO: Else append node after tail
        else:
            self.tail.next = node
            self.tail = self.tail.next # Dani's code in class
            self.size += 1
            # self.tail = self.head
            # while (self.tail.next is not None):
            #     self.tail = self.tail.next

            # self.tail.next = node # puts node on the end as the last node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Why and under what conditions?""" # no loops because head is tracked
        # TODO: Create new node to hold given item
        node = Node(item)
        # node.data = item
        # TODO: Prepend node before head, if it exists
        if self.is_empty():
            self.head = node
            self.tail = node
            self.size = 1
        else:
            node.next = self.head
            self.head = node
            self.size += 1

    def find(self, matcher):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item, if present return True otherwise False
        # node = Node()
        node = self.head # start at the beginning
        # found = False
        # i = 0
        # if node is not None: # while node exists
        while node is not None: # iterate until the end of the list
            if matcher(node.data):
                return node.data
            node = node.next
        return None
        #         i += 1
        #         if node.data == matcher: # matcher is a function
        #             found = True
        #             break
        #         node = node.next # if it is not a match, move on to the next node to check it
        #     if found == True:
        #         print(f'{matcher} found at index {i}')
        #         return node.data
        #     else:
        #         print("item not found")
        # else:
        #     print("The list is empty.")
                    

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        if not self.is_empty():
            if self.head.data == item:
                if self.head is self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                return
                # TODO: Update previous node to skip around node with matching data
            else:
                node = self.head
                while node.next is not None: #while the current node is not the tail
                    if node.next.data == item:
                        if node.next is self.tail:
                            self.tail = node
                        node.next = node.next.next
                        return
                    node = node.next
            # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        
        raise ValueError('Item not found: {}'.format(item))




        # node = self.head # start at the beginning
        # while node: # check that head exists
        #     if node.data == item:
        #         if node.next: # if there is another node after current node:
        #             node.data = node.next.data
        #             node.next = node.next.next
        #         else: # if there is no node after current node:
        #             node = None # delete node?
                
             
        #     node = node.next # if it is not a match, move on to the next node to check it
    

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
