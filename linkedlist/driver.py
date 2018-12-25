from node import *
from ll import *

if __name__ == "__main__":
	list1 = LinkedList()
	list2 = LinkedList()
	list1.headval = Node(0)
	list2.headval = Node(0)

	n1 = Node(1)
	n7 = Node(1)
	n8 = Node(2)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)
	n5 = Node(4)
	n6 = Node(4)

	n9 = Node(1)
	n10 = Node(1)

	list1.add_to_end(n1)
	list1.add_to_end(n8)
	list1.add_to_end(n7)
	list1.add_to_end(n2)
	list1.add_to_end(n4)
	list1.add_to_end(n5)
	list1.add_to_end(n6)

	list2.add_to_end(n9)
	list2.add_to_end(n10)
	# list1.add_to_end(n5)
	# list1.add_to_end(n6)

	# print("Before")
	# list1.list_print()
	# print()

	# list1.rm_dupe()
	# list1.delete(5)

	# list1.reverse()
	# list1.rm_dupe()

	# list1.rm_kth_last(1)

	list1.add_l_to_r(list2)
	# list1.add_r_to_l(list2)




	# print()
	# print("After: ")
	# list1.list_print()