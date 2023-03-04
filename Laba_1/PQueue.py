class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def __heapify(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.size and self.queue[left] > self.queue[largest]:
            largest = left
        if right < self.size and self.queue[right] > self.queue[largest]:
            largest = right

        if largest != index:
            self.queue[index], self.queue[largest] = self.queue[largest], self.queue[index]
            self.__heapify(largest)

    def is_empty(self):
        return True if self.size == 0 else False

    def Qsize(self):
        return self.size

    def push(self, value):
        if self.size == 0:
            self.queue.append(value)
            self.size += 1
        else:
            self.queue.append(value)
            self.size += 1
            for i in range((self.size // 2) - 1, -1, -1):
                self.__heapify(i)

    def pop(self):
        try:
            if self.size == 0:
                raise Exception("Out of range")
            self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
            self.queue.pop()
            self.size -= 1
            self.__heapify(0)

        except Exception:
            return

    def Qprint(self):
        for i in range(self.size):
            print(str(self.max_element()) + " ")
            self.pop()

    def max_element(self):
        if self.is_empty():
            return None
        else:
            return self.queue[0]
