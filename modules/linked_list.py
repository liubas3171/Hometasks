'''Realisation of data structure linked list'''

class Node:
    '''Class for representing node in linked list'''

    def __init__(self, value, link):
        '''(Node, object, Node) -> None
        Create a new Node, where value is object and link is next Node.
        '''
        self.value = value
        self.next = link

    def __str__(self):
        '''Node -> str
        Return str that represents Node in good look.
        '''
        return str(self.value)


class LinkedList:
    '''Class for representing a linked list'''

    def __init__(self):
        '''Create a new empty LinkedList'''
        self._head = None
        self._size = 0

    def __len__(self):
        '''Return length of LinkedList'''
        return self._size

    def add(self, obj):
        '''
        Add obj to first place of LinkedList
        '''
        self._head = Node(obj, self._head)
        self._size += 1

    def __str__(self):
        '''Return str that represents LinkedList'''
        node = self._head
        res = '['
        while node:
            res += str(node.value) + '->'
            node = node.next
        res = res[:-2] + ']'
        return res

    def add_sorted(self, obj, what_compare):
        '''(LinkedList, dict, str) -> None
        Add dict to list, and all dicts in list will
        be sorted by their key what_compare, from bigger to lower.

        >>> dict1= {'a': 1, 'b': 2}
        >>> dict2 = {'b': 1}
        >>> dict3 = {'b': 5, 'x': 'abba'}
        >>> ex = LinkedList()
        >>> ex.add_sorted(dict1, 'b')
        >>> ex.add_sorted(dict2, 'b')
        >>> ex.add_sorted(dict3, 'b')
        >>> str(ex)
        "[{'b': 5, 'x': 'abba'}->{'a': 1, 'b': 2}->{'b': 1}]"
        '''
        node = self._head
        if not node or obj[what_compare] >= node.value[what_compare]:
            self._head = Node(obj, self._head)
        else:
            while node.next and node.next.value[what_compare] > obj[what_compare]:  # <?
                node = node.next
            node.next = Node(obj, node.next)
        self._size += 1

    def __contains__(self, item):
        '''Return True if item is in LinkedList. Return False otherwise'''
        node = self._head
        while node:
            if item == node.value:
                return True
            node = node.next
        return False

    def delete(self, index=0):
        '''(LinkedList, int) -> object
        Delete from list object with given index.

        >>> ex = LinkedList()
        >>> ex.add('a')
        >>> ex.add('b')
        >>> ex.add('c')
        >>> str(ex)
        '[c->b->a]'
        >>> ex.delete(2)
        >>> str(ex)
        '[c->b]'
        '''
        if not 0 <= index <= len(self) - 1:
            raise Exception('Incorrect index')
        if index == 0:
            res = self._head
            self._head = self._head.next
            return res
        i = 0
        node = self._head
        while i != index - 1:
            node = node.next
            i += 1
        node.next = node.next.next
        self._size -= 1

    def __iter__(self):
        '''Return iterator of LinkedList'''
        node = self._head
        while node:
            yield node.value
            node = node.next

    def __getitem__(self, index=0):
        '''(LinkedLIst, int) -> Node
        Return Node with given index.
        '''
        if not 0 <= index <= len(self) - 1:
            raise Exception('Incorrect index')
        node = self._head
        i = 0
        while i != index:
            node = node.next
            i += 1
        return node
