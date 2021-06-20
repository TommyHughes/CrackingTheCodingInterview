#####################################################################
# DATE      06/19/2021
# AUTHOR    Thomas Hughes
# DESCRIPTION
#   These are classes that will be used to solve problems
#   for the Linked List chapter.
#####################################################################

class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList(Node):
    def __init__(self, node):
        self.head = node
        self.current = self.head

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is not None:
            tmp = self.current
            self.current = self.current.next
        else:
            self.current = self.head
            raise StopIteration

        return tmp
    
    def __repr__(self):
        out = ''
        for node in self:
            if node is not None:
                out = out + str(node.value) + ' -> '
        
        return out[:-4]
            