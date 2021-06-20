#####################################################################
# DATE      06/19/2021
# AUTHOR    Thomas Hughes
# INTERVIEW QUESTION
#   2.1 Remove Dupes
#   Write code to remove duplicates from an unsorted linked list.
#   FOLLOW UP
#   How would you solve this problem if a temporary buffer is not
#   allowed?
#####################################################################
from MyClasses.LinkedList import Node, LinkedList

def remove_dupes(linked_list):
    ll = linked_list
    values = {}
    prev = None
    current = ll.head
    for node in ll:
        if (node.value in values) and (prev is not None):
            prev.next = node.next
        else:
            values[node.value]=''
            prev = node

    return ll