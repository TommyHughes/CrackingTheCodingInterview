#####################################################################
# DATE      06/26/2021
# AUTHOR    Thomas Hughes
# DESCRIPTION
#   These are classes related to the stack data structure
#####################################################################

class StackNode(object):
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Stack(StackNode):
    def __init__(self,stack_node):
        self.top = stack_node

    def pop(self):
        if self.top is None: raise AttributeError("Stack cannot pop when empty")
        out = self.top.data
        self.top = self.top.next
        return out
        
    def push(self,data):
        new_top = StackNode(data)
        new_top.next = self.top
        self.top = new_top

    def peek(self):
        if self.top is None: raise AttributeError("Stack cannot peek when empty")
        return self.top.data
    
    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False