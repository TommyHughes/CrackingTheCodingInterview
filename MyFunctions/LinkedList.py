#####################################################################
# DATE      06/19/2021
# AUTHOR    Thomas Hughes
# DESCRIPTION
#   These are functions that will be used to solve problems
#   for the Linked List chapter.
#####################################################################
from MyClasses.LinkedList import LinkedList, Node

def copy_linked_list(ll):
    ll_copy = LinkedList(Node(None))
    for node in ll:
        ll_copy.current.value = node.value
        if node.next is not None:
            ll_copy.current.next = Node(None)
            ll_copy.current = ll_copy.current.next
    return ll_copy

def reverse_linked_list(ll,in_place=True):
    # write a function that reverses a linked list
    prev = None
    tmp = LinkedList(Node(None))
    if in_place is True:
        for node in ll:
            if node.next is None:
                    ll.head = node
            node.next = prev
            prev = node
        return ll
    else:
        for node in ll:
            if node.next is None:
                tmp.head = tmp.current
            tmp.current.next = prev
            prev = tmp.current


def iterable_to_linked_list(iter):
    pass