class Queue:
    def _init_(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self, item):
        self.items.pop(item)

    def is_empty():
        return self.items == []

    def size():
        return len(self.items)