#####################################################################
# DATE      06/26/2021
# AUTHOR    Thomas Hughes
# INTERVIEW QUESTION
#   2.8 Loop Detection
#       Given a circular linked lit, implement an algorithm that
#       returns the node at the beginning of the loop
#       DEFINITION
#       A circular linked list: A (corrupt) linked list in which
#       a node's next pointer points to an earlier node, so as
#       to make a loop in the linked list.
#       EXAMPLE
#       Input: A -> B -> C -> D -> E -> C (same as earlier C)
#       Output: C
#####################################################################
from MyClasses.LinkedList import LinkedList, Node

def linked_list_loop_detection(ll):
    visited = set()
    for node in ll:
        if node in visited:
            return node
        else:
            visited.add(node)
    return None