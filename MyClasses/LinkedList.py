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
    def __init__(self, value):
        self.head = Node(value)