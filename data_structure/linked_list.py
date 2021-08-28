from abc import abstractmethod


class NoSuchElementException(Exception):
    pass


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedListInterface:
    @abstractmethod
    def append(self, node: Node) -> None:
        pass

    @abstractmethod
    def pop(self) -> Node:
        pass

    @abstractmethod
    def shift(self) -> Node:
        pass

    @abstractmethod
    def unshift(self, node: Node) -> None:
        pass


class LinkedList(LinkedListInterface):
    def __init__(self):
        self.head = None

    def append(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            return
        cursor = self.head
        while cursor.next is not None:
            cursor = cursor.next
        cursor.next = node

    def pop(self) -> Node:
        if self.head is None:
            raise NoSuchElementException()
        # 헤드에만 노드가 있는 경우
        if self.head.next is None:
            last_node = self.head
            self.head = None
            return last_node
        node = self.head
        while node.next.next is not None:
            node = node.next
        last_node = node.next
        node.next = None
        return last_node

    def shift(self) -> Node:
        if self.head is None:
            return NoSuchElementException()
        node = self.head
        self.head = self.head.next
        return node

    def unshift(self, node: Node) -> None:
        node.next = self.head
        self.head = node

    def __str__(self):
        current_node = self.head
        if current_node is None:
            return "{}"
        output = "{"
        output += str(current_node.val)
        while current_node.next is not None:
            current_node = current_node.next
            output += " -> "
            output += str(current_node.val)
        output += "}"
        return output


linked_list = LinkedList()

linked_list.append(Node(2))
linked_list.append(Node(1))
linked_list.append(Node(27))
linked_list.append(Node(30))

print(linked_list.shift().val)
print(linked_list.shift().val)
print(linked_list.shift().val)
print(linked_list.shift().val)

linked_list.unshift(Node(3))
linked_list.unshift(Node(2))
linked_list.unshift(Node(1))
linked_list.unshift(Node(56))

print(linked_list)
