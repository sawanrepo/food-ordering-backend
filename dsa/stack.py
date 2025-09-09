class Stack:
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self, item):
        self.items.append(item)
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        self.top -= 1
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.top]

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

    def clear(self):
        self.items = []
        self.top = -1