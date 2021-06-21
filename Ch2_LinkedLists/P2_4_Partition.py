#####################################################################
# DATE      12/02/2020
# AUTHOR    Thomas Hughes
# INTERVIEW QUESTION
#   2.4 Partition
#       Write code to partition a linked list around a value x
#       such that all nodes less than x come before all nodes
#       greater than or equal to x.
#####################################################################
# from classes import Node, LinkedList, iterable_to_LinkedList

# def partition(x,ll):
#     prev = ll.get_head()
#     current = prev.get_nxt()
#     if current is None:
#         return None
#     else:
#         nxt = current.get_nxt()
#     while current is not None:
#         if (current.get_data() < x):
#             prev.set_nxt(nxt)
#             current.set_nxt(ll.get_head())
#             ll.set_head(current)
#             current = nxt
#             if nxt is not None:
#                 nxt = nxt.get_nxt()
#         else:
#             prev = current
#             current = nxt
#             if nxt is not None:
#                 nxt = nxt.get_nxt()

# #ll = iterable_to_LinkedList([9,16,17,16,15,4,3,2,1])
# ll = iterable_to_LinkedList([9,8,7,6,54,3,2,1])
# partition(100,ll)

# for node in ll:
#     print(node.get_data()) #123498765
from MyClasses.LinkedList import Node, LinkedList

def partition(x,linked_list):
    prev = None
    for node in linked_list:
        if (node is not linked_list.head) and (node.value < x):
            prev.next = node.next
            node.next = linked_list.head
            linked_list.head = node
        else:
            prev = node
    
    return linked_list
