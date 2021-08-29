from abc import abstractmethod


class NoSuchElement(Exception):
    pass


class WrongIndex(Exception):
    pass


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        result = "{ "
        result += str(self.val)
        result += " }"
        return result


class DoublyLinkedListInterface:
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

    @abstractmethod
    def search(self, index: int) -> None:
        pass

    @abstractmethod
    def insert(self, index: int, node: Node) -> None:
        pass

    @abstractmethod
    def remove(self, index: int) -> Node:
        pass


class DoublyLinkedList(DoublyLinkedListInterface):
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
            node.prev = self.last
            self.last = node
        self.size += 1
        return

    def pop(self) -> Node:
        if self.size == 0:
            raise NoSuchElement()
        if self.size == 1:
            node = self.last
            self.first = None
            self.last = None
            self.size -= 1
            return node
        node = self.last
        prev_node = self.last.prev
        prev_node.next = None
        node.prev = None
        self.last = prev_node
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
        next_node.prev = None
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
            self.first.prev = node
            self.first = node
        self.size += 1
        return

    def search(self, index: int) -> None:
        if index < 0 or self.size - 1 < index:
            raise WrongIndex()
        if self.size == 0:
            raise NoSuchElement()
        node = self.first
        start_index = 0
        while start_index != index:
            node = node.next
            start_index += 1
        return node

    def insert(self, index: int, node: Node) -> None:
        if index < 0 and self.size < index:
            raise WrongIndex()
        elif index == 0:
            self.unshift(node)
        elif index == self.size:
            self.append(node)
        else:
            found_node = self.search(index)
            prev_node = found_node.prev
            prev_node.next = node
            found_node.prev = node
            node.prev = prev_node
            node.next = found_node
            self.size += 1
        return

    def remove(self, index: int) -> Node:
        if index < 0 and self.size - 1 < index:
            raise WrongIndex()
        elif index == 0:
            self.shift()
        elif index == self.size - 1:
            self.pop()
        else:
            found_node = self.search(index)
            prev_node = found_node.prev
            next_node = found_node.next
            found_node.prev = None
            found_node.next = None
            prev_node.next = next_node
            next_node.prev = prev_node
            self.size -= 1
        return found_node

    def __str__(self) -> str:
        if self.size == 0:
            return "<- None ->"

        node = self.first

        result = ""
        result += "None <- "
        result += str(node.val)
        result += " -> "

        while node.next is not None:
            node = node.next
            result += "<- "
            result += str(node.val)
            result += " -> "
        result += "None"
        return result


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

doubly_linked_list = DoublyLinkedList()

doubly_linked_list.unshift(node1)
doubly_linked_list.append(node5)

print(doubly_linked_list.search(1))

doubly_linked_list.insert(1, node2)
doubly_linked_list.insert(2, node3)
doubly_linked_list.insert(3, node4)

print(doubly_linked_list.remove(3))

print(doubly_linked_list)
