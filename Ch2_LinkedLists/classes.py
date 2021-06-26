#####################################################################
# DATE      11/14/2020
# AUTHOR    Thomas Hughes
# DESCRIPTION
#   These are classes that will be used to solved problems
#   for the Linked List chapter.
#####################################################################

class Node(object):
    def __init__(self,data):
        self._data = data
        self._nxt = None
    
    def get_data(self):
        return self._data
    
    def get_nxt(self):
        return self._nxt
    
    def set_data(self,data):
        self._data = data

    def set_nxt(self,nxt):
        self._nxt = nxt

class LinkedList(object):
    def __init__(self,head):
        self._head = head
        self._current = self._head

    def __iter__(self):
        self.set_current(self.get_head())
        return self

    def __next__(self):
        tmpNode = self.get_current()
        if (self.get_current() is None):
            raise StopIteration
        else:
            self.set_current(self.get_current().get_nxt())
        return tmpNode
    
    def get_head(self):
        return self._head

    def set_head(self, n):
        self._head = n

    def get_current(self):
        return self._current
    
    def set_current(self, n):
        self._current = n

def iterable_to_LinkedList(iterable):
    tmp = None
    ll = LinkedList(Node(""))
    for item in iterable:
        if tmp is None:
            ll.set_head(Node(item))
            ll.set_current(ll.get_head())
        else:
            tmp.set_nxt(Node(item))
            ll.set_current(tmp.get_nxt())
        tmp = ll.get_current()
    return ll