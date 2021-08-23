from abc import abstractmethod
import sys


class Node:
    def __init__(self, val, count):
        self.val = val
        self.count = count
        self.next = None
        self.prev = None

    def __str__(self):
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
    def search(self, index) -> Node:
        pass

    @abstractmethod
    def __str__(self):
        pass


class NoSuchElementException(Exception):
    pass


class WrongIndex(Exception):
    pass


class Queue(QueueInterface):
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, node: Node) -> None:
        if self.size == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            node.prev = self.last
            self.last = node
        self.size += 1
        return

    def dequeue(self) -> Node:
        if self.size == 0:
            raise NoSuchElementException()
        if self.size == 1:
            node = self.first
            self.first = None
            self.last = None
        else:
            node = self.first
            self.first = self.first.next
            self.first.prev = None
            node.next = None
        self.size -= 1
        return node

    def search(self, index) -> Node:
        if index < 0 or index > self.size - 1:
            raise WrongIndex()
        start_index = 0
        node = self.first
        while start_index != index:
            start_index += 1
            node = node.next
        return node

    def peek(self) -> Node:
        if self.size == 0:
            raise NoSuchElementException()
        return self.first

    def __str__(self):
        node = self.first
        result = "None "
        while node is not None:
            result += "<- "
            result += str(node.val)
            result += " -> "
            node = node.next
        result += "None"
        return result


N, K = map(int, sys.stdin.readline().split())

visited = [False] * (K + 1)

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))


def bfs(coins, target_value):
    value_queue = Queue()
    for coin in coins:
        if coin <= target_value:
            value_queue.enqueue(Node(coin, 1))
            visited[coin] = True
    while value_queue.size > 0:
        node = value_queue.dequeue()
        if node.val == target_value:
            return node.count
        for coin in coins:
            cum = node.val + coin
            cnt = node.count + 1
            if cum > target_value:
                continue
            elif cum <= target_value and visited[cum] == False:
                value_queue.enqueue(Node(cum, cnt))
                visited[cum] = True
    return -1


print(bfs(coins, K))
