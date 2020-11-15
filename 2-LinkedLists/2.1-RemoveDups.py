#####################################################################
# DATE      11/14/2020
# AUTHOR    Thomas Hughes
# INTERVIEW QUESTION
#   2.1 Remove Dupes
#   Write code to remove duplicates from an unsorted linked list.
#   FOLLOW UP
#   How would you solve this problem if a temporary buffer is not
#   allowed?
#####################################################################
from classes import Node, LinkedList, iterable_to_LinkedList

def remove_dups(ll):
    uniques = set({})
    for node in ll:
        uniques.add(node.get_data()) # sets don't allow repeat elements
    return iterable_to_LinkedList(uniques)

ll = remove_dups(iterable_to_LinkedList([1,1,1,1,1,1,1]))

for node in ll:
    print(node.get_data())

