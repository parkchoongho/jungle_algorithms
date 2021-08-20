import sys
from abc import abstractmethod

N, M = map(int, sys.stdin.readline().split())


input_list = []

for _ in range(N):
    input_list.append(list(map(int, sys.stdin.readline().rstrip())))

visited = [[False] * M for _ in range(N)]


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
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


def bfs(x, y):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = Queue()
    queue.enqueue(Node(x, y))
    visited[x][y] = True
    while queue.size > 0:
        adj_node = queue.dequeue()
        for i in range(4):
            nx = adj_node.x + dx[i]
            ny = adj_node.y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if input_list[nx][ny] == 0:
                continue

            if input_list[nx][ny] == 1:
                if not visited[nx][ny]:
                    input_list[nx][ny] = input_list[adj_node.x][adj_node.y] + 1
                    queue.enqueue(Node(nx, ny))
                    visited[nx][ny] = True

    return input_list[N - 1][M - 1]


print(bfs(0, 0))
