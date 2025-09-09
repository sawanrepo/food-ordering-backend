class HashMap:
    def __init__(self, size=1000):
        self.size = size
        self.buckets = [None] * size
        self.count = 0

    def _hash(self, key):
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            return sum(ord(char) for char in key) % self.size
        else:
            raise ValueError("Key must be int or str")

    def put(self, key, value):
        index = self._hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = []
        
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        
        self.buckets[index].append((key, value))
        self.count += 1

    def get(self, key):
        index = self._hash(key)
        if self.buckets[index] is None:
            return None
        
        for k, v in self.buckets[index]:
            if k == key:
                return v
        
        return None

    def remove(self, key):
        index = self._hash(key)
        if self.buckets[index] is None:
            return False
        
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]
                self.count -= 1
                return True
        
        return False

    def __len__(self):
        return self.count

    def __contains__(self, key):
        return self.get(key) is not None