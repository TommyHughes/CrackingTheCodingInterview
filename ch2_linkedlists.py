from MyClasses.LinkedList import Node, LinkedList
from Ch2_LinkedLists.P2_1_RemoveDupes import remove_dupes

# 2.1 Remove Dupes
ll = LinkedList(Node(10))
second = Node(55)
ll.head.next = second
third = Node(10)
second.next = third
# fourth = Node(11)
# third.next = fourth
# fifth = Node(1)
# fourth.next = fifth


print("first: ",ll.current.value)
print("second: ",ll.current.next.value)
print("third: ",ll.current.next.next.value)
print("fourth: ",ll.current.next.next.next)

print("====FOR LOOP===")

for node in ll:
    if node is not None:
        print(node.current.value)