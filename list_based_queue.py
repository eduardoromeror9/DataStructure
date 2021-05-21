

class ListQueue:
    def __init__(self):
        self.items = []
        self.zize = 0
        
    def enqueue(self, data):
        self.items.insert(0, data)
        self.zize += 1
    
    def dequeue(self):
        data = self.items.pop()
        self.zize += 1
        return data

    def traverse(self):
        total_items = self.zize
        
        for item in range(total_items):
            print(self.items[item])