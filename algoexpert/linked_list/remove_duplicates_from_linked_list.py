# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	current_node = linkedList
	while current_node is not None:
		next_node = current_node.next
		while next_node is not None and current_node.value == next_node.value:
			next_node = next_node.next
			
		current_node.next = next_node
		current_node = next_node
		
		
    return linkedList
