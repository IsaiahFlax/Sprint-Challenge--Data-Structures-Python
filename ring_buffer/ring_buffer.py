class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.tail = -1
        self.head = 0
        self.size = 0

    def append(self, item):
        if self.size == self.capacity:
            self.current = item
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.queue[self.tail] = item
            self.size +1
            

    def get(self):
        a = []
        for i in self.queue:
            if i is not None:
                a.append(i)
        return a