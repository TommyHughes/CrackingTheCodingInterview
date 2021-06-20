from MyClasses.LinkedList import Node, LinkedList
from Ch2_LinkedLists.P2_1_RemoveDupes import remove_dupes
from Ch2_LinkedLists.P2_2_ReturnKthToLast import kth_to_last

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

problem_user_wants = input("Which problem output would you like to see (ex P2_1) ")

if problem_user_wants == 'P2_1':
    P2_1()
elif problem_user_wants == 'P2_2':
    P2_2()
else:
    print("sorry that problem doesn't exist.")