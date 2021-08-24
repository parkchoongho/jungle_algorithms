from abc import abstractmethod
import sys


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


N, M = map(int, sys.stdin.readline().split())

iceberg_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

count_year = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    count_year += 1

    water_count = [[0] * M for _ in range(N)]

    for x in range(N):
        for y in range(M):
            if iceberg_map[x][y] > 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and iceberg_map[nx][ny] == 0:
                        water_count[x][y] += 1

    for x in range(N):
        for y in range(M):
            iceberg_map[x][y] -= water_count[x][y]
            if iceberg_map[x][y] < 0:
                iceberg_map[x][y] = 0

    visited = [[False] * M for _ in range(N)]
    bfs_count = 0

    for x in range(N):
        for y in range(M):
            if iceberg_map[x][y] > 0 and not visited[x][y]:
                bfs_count += 1
                connect_queue = Queue()
                connect_queue.enqueue(Node(x, y))
                visited[x][y] = True

                while connect_queue.size > 0:
                    node = connect_queue.dequeue()

                    for i in range(4):
                        nx = node.x + dx[i]
                        ny = node.y + dy[i]

                        if 0 <= nx < N and 0 <= ny < M and iceberg_map[nx][ny] > 0 and not visited[nx][ny]:
                            connect_queue.enqueue(Node(nx, ny))
                            visited[nx][ny] = True

    if bfs_count > 1:
        break

    total = 0

    for i in iceberg_map:
        total += sum(i)

    if total == 0:
        print(0)
        exit()

print(count_year)
