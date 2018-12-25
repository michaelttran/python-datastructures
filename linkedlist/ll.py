from node import *

class LinkedList:
	def __init__(self):
		self.headval = None

	def list_print(self):
		printval = self.headval
		l = ""
		while printval is not None:
			# print(printval.val)
			if(printval.next is not None):
				l += str(printval.val) + ", "
			else:
				l += str(printval.val)
			printval = printval.next

		print(l)


	def add_to_end(self, node):
		curr = self.headval

		if(curr.next is None):
			curr.next = node
		else:
			while curr is not None:
				if(curr.next is None):
					curr.next = node
					break
				curr = curr.next


	def delete(self, val):
		curr = prev = self.headval
		found = False

		# If ll doesn't exist
		if( curr is None):
			print("Linked List doesn't exist")
			exit()

		# Head case
		if(curr.val == val):
			self.headval = self.headval.next

		# Body case
		while curr is not None:

			if( curr.val == val):
				prev.next = curr.next
				found = True


			prev = curr
			curr = curr.next

		if(found == False):
			print(val, "wasn't in the linked list")



	def rm_dupe(self):
		curr = prev = self.headval
		
		seen = []

		# One pass through to add seen nodes to list
		while curr is not None:
			if( curr.val in seen):
				prev.next = curr.next
				curr = prev


			if( curr.val not in seen):
				seen.append(curr.val)



			prev = curr
			curr = curr.next

		print("Finished deleting duplicates")
		print()

	def reverse(self):
		curr = self.headval
		tmp = LinkedList()
		tmp.headval = Node(curr.val)
		curr = curr.next

		while curr is not None:
			tNode = Node(curr.val)
			tNode.next = tmp.headval
			tmp.headval = tNode
			curr = curr.next

		print("Reversed LL: ")
		tmp.list_print()

		self.headval = tmp.headval

	# DEV NOTE: Not sure if kth to last should start at 0 or 1. Going to assume 0 because of CS
	def rm_kth_last(self, num):
		curr = prev = self.headval
		lLength = 0
		i = 0

		# One pass through to find length of the linked list
		while curr is not None:
			lLength += 1
			curr = curr.next

		curr = self.headval
		pos = lLength - num - 1
		# Formula for kth to last: length - num = index that should be deleted
		while curr is not None:
			if(i == pos):
				print("The", num, "to last element is", curr.val)
			i += 1
			prev = curr
			curr = curr.next

	def add_l_to_r(self, h2):
		# self.list_print()
		# h2.list_print()
		num1 = ""
		num2 = ""
		curr = self.headval
		curr2 = h2.headval
		while curr is not None:
			num1 += str(curr.val)
			curr = curr.next

		while curr2 is not None:
			num2 += str(curr2.val)
			curr2 = curr2.next

		total = int(num1) + int(num2)
		print("ll1: ")
		self.list_print()
		print("ll2: ")
		h2.list_print()

		print()
		print("The sum of the two linked lists from left to right: ", total)




	


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




# print()
# print("After: ")
# list1.list_print()
