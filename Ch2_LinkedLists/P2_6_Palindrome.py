#####################################################################
# DATE      12/17/2020
# AUTHOR    Thomas Hughes
# INTERVIEW QUESTION
#   2.6 Palindrome
#       Implement a function to check if a linked list is
#       a palindrome.
#####################################################################
# from classes import Node, LinkedList, iterable_to_LinkedList

# def isPalindrome(ll):
#     ll.set_current(ll.get_head())
#     #reverse ll
#     old_node = None
#     new_node = old_node
#     length = 0
#     for node in ll:
#         length += 1
#         new_node = Node(node.get_data())
#         new_node.set_nxt(old_node)
#         old_node = new_node
    
#     reversed_ll = LinkedList(new_node)

#     ll.set_current(ll.get_head())
#     reversed_ll.set_current(reversed_ll.get_head())
#     result = True
#     index = 1
#     while ((index<=(length//2)) and (result==True)):
#         if (ll.get_current().get_data()!=reversed_ll.get_current().get_data()):
#             result = False
        
#         index += 1
#         ll.set_current(ll.get_current().get_nxt())
#         reversed_ll.set_current(reversed_ll.get_current().get_nxt())
#     return result

# ll = iterable_to_LinkedList("racecar")

# print(isPalindrome(ll)) #true
from MyClasses.LinkedList import LinkedList, Node
from MyFunctions.LinkedList import copy_linked_list, reverse_linked_list

def is_palindrome(ll):
    result = True
    ll_reversed = reverse_linked_list(copy_linked_list(ll))
    while ((result is True) and (ll.current is not None)):
        if ll.current.value != ll_reversed.current.value:
            result = False
        next(ll)
        next(ll_reversed)
    ll.current = ll.head
    return result
