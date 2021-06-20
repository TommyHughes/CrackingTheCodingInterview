#####################################################################
# DATE      12/01/2020
# AUTHOR    Thomas Hughes
# INTERVIEW QUESTION
#   2.2 Return Kth To Last
#       Implement an algorithm to find the kth to last element
#       of a singly linked list.
#####################################################################
# from classes import Node, LinkedList, iterable_to_LinkedList

# def kth_to_last(k,ll):
#     count = 1
#     Runner = ll.get_head()
#     Pointer = ll.get_head()
#     while Runner.get_nxt() is not None:
#         Runner = Runner.get_nxt()
#         count += 1
#         if (k < count):
#             Pointer = Pointer.get_nxt()
    
#     if (count < k):
#         raise ValueError("List too short")
#     else:
#         return Pointer.get_data()

# ll = iterable_to_LinkedList([1,2,3,4,5])

# for i in range(1,6):
#     print("The {}th to last is ".format(i),kth_to_last(i,ll)) #5,4,3,2,1


from MyClasses.LinkedList import Node, LinkedList

def kth_to_last(k,ll):
    values = []
    for node in ll:
        values.append(node.value)
    
    if len(values) < k:
        return None
    else:
        return(values[len(values)-(k-1)-1])