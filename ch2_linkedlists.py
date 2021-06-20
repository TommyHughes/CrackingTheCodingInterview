from MyClasses.LinkedList import Node, LinkedList
from Ch2_LinkedLists.P2_1_RemoveDupes import remove_dupes

# 2.1 Remove Dupes
ll = LinkedList(10)
ll.next = Node(10)
ll.next.next = Node(8)
ll.next.next.next = Node(3)
ll.next.next.next.next = Node(8)

ll_no_dupes = remove_dupes(ll)
print(ll_no_dupes is None)
print(ll_no_dupes.value)
print(ll_no_dupes.next.value)
print(ll_no_dupes.next.next.value)
# node = ll_no_dupes
# while node is not None:
#     print(node.value)
#     node = node.next
for node in ll_no_dupes:
    print(node.value)
