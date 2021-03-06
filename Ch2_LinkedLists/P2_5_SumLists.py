#####################################################################
# DATE      12/16/2020
# AUTHOR    Thomas Hughes
# INTERVIEW QUESTION
#   2.5 SumLists
#       You have two numbers represented by a linked list,
#       where each node contains a single digit. The digits
#       are stored in reverse order, such that the 1's digit
#       is at the head of the list. Write a function that
#       adds the two numbers and returns the sum as a
#       linked list.
#####################################################################
# from classes import Node, LinkedList, iterable_to_LinkedList

# def sumLists(llA,llB):
#     llA.set_current(llA.get_head())
#     llB.set_current(llB.get_head())
#     result = LinkedList(Node(None))
#     carry = 0
#     while (not (llA.get_current() is None and llB.get_current() is None)):
#         if llA.get_current() is None:
#             a_i = 0
#         else:
#             a_i = llA.get_current().get_data()
#             llA.set_current(llA.get_current().get_nxt())
        
#         if llB.get_current() is None:
#             b_i = 0
#         else:
#             b_i = llB.get_current().get_data()
#             llB.set_current(llB.get_current().get_nxt())

#         total = a_i + b_i + carry
#         result.get_current().set_data(total%10)

#         if (total > 9):
#             carry = 1
#         else:
#             carry = 0

#         if (not (llA.get_current() is None and llB.get_current() is None)):
#             result.get_current().set_nxt(Node(None))
#             result.set_current(result.get_current().get_nxt())
    
#     if carry is 1:
#         result.get_current().set_nxt(Node(1))

#     return result

# llA = iterable_to_LinkedList([9,9,9])
# llB = iterable_to_LinkedList([9,9,9,9,9,9,9,9])

# answer = sumLists(llA,llB)

# for node in answer:
#     print(node.get_data())
from MyClasses.LinkedList import Node, LinkedList
from MyFunctions.LinkedList import reverse_linked_list

def sum_lists(ll_a,ll_b):
    # write a function that adds up the values in two linked lists
    carry = 0
    ll_a.current = ll_a.head
    ll_b.current = ll_b.head
    ll_sum = LinkedList(Node(None))
    while not (ll_a.current is None and ll_b.current is None):
        if ll_a.current is not None:
            term_a = ll_a.current.value
            ll_a.current = ll_a.current.next
        else:
            term_a = 0
        
        if ll_b.current is not None:
            term_b = ll_b.current.value
            ll_b.current = ll_b.current.next
        else:
            term_b = 0
        
        digit = (term_a + term_b) % 10
        ll_sum.current.value = digit + carry

        if 10 <= (term_a + term_b):
            carry = 1
        else:
            carry = 0
        
        if (carry is 1) or (not (ll_a.current is None and ll_b.current is None)):
            ll_sum.current.next = Node(None)
            ll_sum.current = ll_sum.current.next
        
    
    ll_a.current = ll_a.head
    ll_b.current = ll_a.head
    ll_sum.current = ll_sum.head
    return ll_sum
