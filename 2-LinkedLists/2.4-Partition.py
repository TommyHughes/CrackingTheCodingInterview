#####################################################################
# DATE      12/02/2020
# AUTHOR    Thomas Hughes
# INTERVIEW QUESTION
#   2.3 Partition
#       Write code to partition a linked list around a value x
#       such that all nodes less than x come before all nodes
#       greater than or equal to x.
#####################################################################
from classes import Node, LinkedList, iterable_to_LinkedList

def partition(x,ll):
    prev = None
    current = ll.get_head()
    nxt = current.get_nxt()
    while current is not None:
        if (current.get_data() < x):
            if prev is not None:
                prev.set_nxt(current.get_nxt())
            else:
                prev = current
            current.set_nxt(ll.get_head())
            ll.set_head(current)
            current = nxt
            if nxt is not None:
                nxt = nxt.get_nxt()
        else:
            prev = current
            current = nxt
            if nxt is not None:
                nxt = nxt.get_nxt()

ll = iterable_to_LinkedList([9,8,7,6,5,4,3,2,1])

partition(5,ll)

for node in ll:
    print(node.get_data()) #123498765