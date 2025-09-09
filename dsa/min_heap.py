class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)][0] > self.heap[i][0]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def heapify_down(self, i):
        n = len(self.heap)
        while True:
            left = self.left_child(i)
            right = self.right_child(i)
            smallest = i
            
            if left < n and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < n and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            
            if smallest != i:
                self.swap(i, smallest)
                i = smallest
            else:
                break
    
    def insert(self, key, value):
        self.heap.append((key, value))
        self.heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        if not self.heap:
            return None
        
        min_item = self.heap[0]
        last_item = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_item
            self.heapify_down(0)
        
        return min_item
    
    def peek_min(self):
        return self.heap[0] if self.heap else None
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0