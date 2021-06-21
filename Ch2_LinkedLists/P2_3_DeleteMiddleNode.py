#####################################################################
# DATE      12/01/2020
# AUTHOR    Thomas Hughes
# INTERVIEW QUESTION
#   2.3 Delete Middle Node
#       Implement an algorithm to delete any node in the middle
#       (i.e any node but the first and last) of a singly linked
#       list given only access to that node.
#####################################################################
# from classes import Node, LinkedList, iterable_to_LinkedList

# def delete_middle_node(n):
#     n.set_data(n.get_nxt().get_data())
#     n.set_nxt(n.get_nxt().get_nxt())
    


# ll = iterable_to_LinkedList(["a","b","c","d"])

# input = ll.get_head()
# for i in range(0,2):
#     input = input.get_nxt()

# for n in ll:
#     print(n.get_data()) #abd

from MyClasses.LinkedList import Node, LinkedList

def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next