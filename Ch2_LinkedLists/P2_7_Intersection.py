#####################################################################
# DATE      06/26/2021
# AUTHOR    Thomas Hughes
# INTERVIEW QUESTION
#   2.7 Intersection
#       Given two (singly) linked lists, determine if the two lists
#       intersect. Return the intersecting node.
#####################################################################
from MyClasses.LinkedList import LinkedList, Node

def linked_list_intersection(ll_a,ll_b):
    for node_a in ll_a:
        for node_b in ll_b:
            if node_a == node_b:
                return node_a
    return None