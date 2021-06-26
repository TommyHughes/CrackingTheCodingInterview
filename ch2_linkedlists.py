from MyClasses.LinkedList import Node, LinkedList
from Ch2_LinkedLists.P2_1_RemoveDupes import remove_dupes
from Ch2_LinkedLists.P2_2_ReturnKthToLast import kth_to_last
from Ch2_LinkedLists.P2_3_DeleteMiddleNode import delete_middle_node
from Ch2_LinkedLists.P2_4_Partition import partition
from Ch2_LinkedLists.P2_5_SumLists import reverse_linked_list, sum_lists
from Ch2_LinkedLists.P2_6_Palindrome import is_palindrome
from Ch2_LinkedLists.P2_7_Intersection import linked_list_intersection

def P2_1():
    # 2.1 Remove Dupes
    ll = LinkedList(Node(10))
    second = Node(55)
    ll.head.next = second
    third = Node(10)
    second.next = third
    fourth = Node(11)
    third.next = fourth
    fifth = Node(1)
    fourth.next = fifth

    print('===Linked List Representation===')
    print(ll)
    print('================================')

    print('===FOR LOOP===')
    for node in ll:
        print(node.value)
    print('==============')

    print('===NO DUPES===')
    remove_dupes(ll)
    print(ll)
    print('==============')

def P2_2():
    #2.2 Kth to Last
    ll = LinkedList(Node(10))
    second = Node(55)
    ll.head.next = second
    third = Node(10)
    second.next = third
    fourth = Node(11)
    third.next = fourth
    fifth = Node(1)
    fourth.next = fifth
    
    print(kth_to_last(int(input("pick your k ")),ll))

def P2_3():
    #2.3 Delete Middle Node
    ll = LinkedList(Node(10))
    second = Node(55)
    ll.head.next = second
    third = Node(10)
    second.next = third
    fourth = Node(11)
    third.next = fourth
    fifth = Node(1)
    fourth.next = fifth

    delete_middle_node(second)
    print(ll)

def P2_4():
    #2.4 Partition
    ll = LinkedList(Node(10))
    second = Node(55)
    ll.head.next = second
    third = Node(10)
    second.next = third
    fourth = Node(11)
    third.next = fourth
    fifth = Node(1)
    fourth.next = fifth

    partition(11,ll)
    print(ll)

def P2_5():
    #2.5 SumLists
    ll_a = LinkedList(Node(2))
    a_second = Node(1)
    ll_a.head.next = a_second
    a_third = Node(5)
    a_second.next = a_third

    ll_b = LinkedList(Node(1))
    b_second = Node(2)
    ll_b.head.next = b_second

    print("Linked List A: ",ll_a)
    reverse_linked_list(ll_a)
    print("Reversed Linked List A: ",ll_a)

    print("Linked List B: ",ll_b)
    reverse_linked_list(ll_b)
    print("Reversed Linked List B: ",ll_b)

    ll_sum = sum_lists(ll_a,ll_b)
    print("Sum of Lists: ",ll_sum)
    reverse_linked_list(ll_sum)
    print("Reversed Sum of Lists: ",ll_sum)

def P2_6():
    # 2.6 Palindrome
    ll = LinkedList(Node('a'))
    second = Node('b')
    ll.head.next = second
    third = Node('c')
    second.next = third

    print(ll)
    print(is_palindrome(ll))

def P2_7():
    # 2.7 Intersection
    ll_a = LinkedList(Node(1))
    a_second = Node(2)
    ll_a.head.next = a_second
    a_third = Node(3)
    a_second.next = a_third

    ll_b = LinkedList(Node(3))
    b_second = a_second
    ll_b.head.next = b_second
    b_third = Node(1)
    b_second = b_third

    print("Linked List A: ",ll_a)
    print("Linked List B: ",ll_b)
    print("Intersection: ",linked_list_intersection(ll_a,ll_b).value)

problem_user_wants = input("Which problem output would you like to see (ex P2_1) ")

if problem_user_wants == 'P2_1':
    P2_1()
elif problem_user_wants == 'P2_2':
    P2_2()
elif problem_user_wants == 'P2_3':
    P2_3()
elif problem_user_wants == 'P2_4':
    P2_4()
elif problem_user_wants == 'P2_5':
    P2_5()
elif problem_user_wants == 'P2_6':
    P2_6()
elif problem_user_wants == 'P2_7':
    P2_7()
else:
    print("sorry that problem doesn't exist.")