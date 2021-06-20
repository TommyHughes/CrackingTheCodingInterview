from MyClasses.LinkedList import Node, LinkedList
from Ch2_LinkedLists.P2_1_RemoveDupes import remove_dupes

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