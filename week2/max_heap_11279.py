import sys


from abc import abstractmethod


class PriorityQueueInterface:
    @abstractmethod
    def insert(self, value: int) -> None:
        pass

    @abstractmethod
    def delete(self) -> int:
        pass

    @abstractmethod
    def heapify(self) -> None:
        pass

    @abstractmethod
    def peek(self) -> int or None:
        pass


class PriorityQueue(PriorityQueueInterface):
    def __init__(self):
        self.data_list = []

    def insert(self, value: int) -> None:
        self.data_list.append(value)
        position = len(self.data_list) - 1
        while position > 0:
            parent = (position - 1) // 2
            if self.data_list[position] > self.data_list[parent]:
                self.data_list[position], self.data_list[parent] = self.data_list[parent], self.data_list[position]
            else:
                break
            position = parent

    def delete(self) -> int:
        if len(self.data_list) == 0:
            return 0
        if len(self.data_list) == 1:
            return self.data_list.pop()
        self.data_list[0], self.data_list[-1] = self.data_list[-1], self.data_list[0]
        value = self.data_list.pop()
        self.heapify()
        return value

    def heapify(self) -> None:
        max = self.data_list[0]

        parent = 0

        while parent < len(self.data_list) // 2:
            left_child = 2 * parent + 1
            right_child = left_child + 1
            child = right_child if right_child <= len(self.data_list) - 1 and self.data_list[right_child] > self.data_list[left_child] else left_child
            if max > self.data_list[child]:
                break
            self.data_list[parent] = self.data_list[child]
            parent = child
        self.data_list[parent] = max

    def peek(self) -> int:
        if len(self.data_list) == 0:
            return
        return self.data_list[0]


priority_queue = PriorityQueue()


test_num = int(sys.stdin.readline())

for _ in range(test_num):
    num = int(sys.stdin.readline())
    if num == 0:
        print(priority_queue.delete())
    else:
        priority_queue.insert(num)
