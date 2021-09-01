from abc import abstractmethod


class NoSuchElement(Exception):
    pass


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def __str__(self) -> str:
        result = "{ "
        result += str(self.val)
        result += " }"


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
    def __init__(self) -> None:
        self.size = 0
        self.first = None
        self.last = None

    def append(self, node: Node) -> None:
        if self.size == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1
        return

    def pop(self) -> Node:
        if self.size == 0:
            raise NoSuchElement()
        if self.size == 1:
            node = self.first
            self.first = None
            self.last = None
            self.size -= 1
            return node
        before_node = self.first
        node = before_node.next
        while node.next is not None:
            before_node = before_node.next
            node = node.next
        before_node.next = None
        self.last = before_node
        self.size -= 1
        return node

    def shift(self) -> Node:
        if self.size == 0:
            raise NoSuchElement()
        if self.size == 1:
            node = self.first
            self.first = None
            self.last = None
            self.size -= 1
            return node
        node = self.first
        next_node = node.next
        node.next = None
        self.first = next_node
        self.size -= 1
        return node

    def unshift(self, node: Node) -> None:
        if self.size == 0:
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node
        self.size += 1
        return

    def __str__(self) -> str:
        if self.size == 0:
            return 'None'
        node = self.first
        result = ""
        result += "{ "
        result += str(node.val)
        result += " }"
        result += " -> "
        while node.next is not None:
            node = node.next
            result += "{ "
            result += str(node.val)
            result += " }"
            result += " -> "
        result += "None"
        return result


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
