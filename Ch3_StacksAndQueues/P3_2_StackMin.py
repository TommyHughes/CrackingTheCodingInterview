#####################################################################
# DATE      06/27/2021
# AUTHOR    Thomas Hughes
# INTERVIEW QUESTION
#   2.8 Stack Min
#####################################################################
from MyClasses.Stack import StackNode, Stack

class StackNodeMin(StackNode):
    def __init__(self, data):
        super().__init__(data)
        self.prev_min = None

class StackMin(Stack):
    def min(self):
        return min(self.top.data,self.top.prev_min)
    
    def push(self,data):
        super().push(data)
        if self.top.next is not None:
            self.top.prev_min = min(self.top.next.data, self.top.next.prev_min)