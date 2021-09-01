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


class QueueInterface:
    @abstractmethod
    def enqueue(self, node: Node) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> Node:
        pass

    @abstractmethod
    def search(self, index: int) -> Node:
        pass

    @abstractmethod
    def peek(self) -> Node or None:
        pass


class Queue(QueueInterface):
    def __init__(self) -> None:
        self.size = 0
        self.first = None
        self.last = None

    def enqueue(self, node: Node) -> None:
        if self.size == 0:
            self.last = node
            self.first = node
        else:
            node.prev = self.last
            self.last.next = node
            self.last = node
        self.size += 1
        return

    def dequeue(self) -> Node:
        if self.size == 0:
            raise NoSuchElement()
        if self.size == 1:
            node = self.first
            self.first = None
            self.last = None
        else:
            node = self.first
            next_node = self.first.next
            node.next = None
            next_node.prev = None
            self.first = next_node
        self.size -= 1
        return node

    def search(self, index: int) -> Node:
        if index < 0 or index > self.size - 1:
            raise WrongIndex()
        if self.size == 0:
            raise NoSuchElement()
        start_index = 0
        node = self.first
        while start_index != index:
            node = node.next
            start_index += 1
        return node

    def peek(self) -> Node or None:
        if self.size == 0:
            raise NoSuchElement()
        return self.first

    def __str__(self) -> str:
        node = self.first
        result = "None"
        while node is not None:
            result += "<- "
            result += str(node.val)
            result += " ->"
            node = node.next
        result += 'None'
        return result


queue = Queue()

queue.enqueue(Node(1))
queue.enqueue(Node(2))
queue.enqueue(Node(3))
queue.enqueue(Node(4))

print(queue.dequeue())
print(queue.dequeue())

print(queue.peek())

print(queue.search(0))

print(queue)
