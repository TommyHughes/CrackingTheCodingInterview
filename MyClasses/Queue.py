#####################################################################
# DATE      06/26/2021
# AUTHOR    Thomas Hughes
# DESCRIPTION
#   These are classes related to the Queue data structure.
#####################################################################

class QueueNode(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue(QueueNode):
    def __init__(self,qnode):
        self.top = qnode
        self.bottom = self.top

    def add(self,data):
        if self.bottom is None:
            self.top = QueueNode(data)
            self.bottom = self.top
        else:
            self.bottom.next = QueueNode(data)
            self.bottom = self.bottom.next

    def remove(self):
        if self.top is None: raise AttributeError('Queue cannot remove when empty')
        out = self.top.data
        self.top = self.top.next
        if self.top is None:
            self.bottom = None
        return out
    
    def peek(self):
        if self.top is None: raise AttributeError('Queue cannot peek when empty')
        return self.top.data

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False