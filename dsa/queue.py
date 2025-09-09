class Queue:
    def __init__(self):
        self.items = []
        self.front = 0
        self.rear = -1

    def enqueue(self, item):
        self.items.append(item)
        self.rear += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self.items[self.front]
        self.front += 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.front]

    def is_empty(self):
        return self.front > self.rear

    def size(self):
        return self.rear - self.front + 1

    def clear(self):
        self.items = []
        self.front = 0
        self.rear = -1