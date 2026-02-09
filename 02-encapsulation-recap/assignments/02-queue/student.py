class Queue:
    def __init__(self):
        self.__items = []   
    def add(self, item):
        self.__items.append(item)
    def next(self):
        if self.is_empty():
            return None
        return self.__items.pop(0)
    def is_empty(self):
        return len(self.__items) == 0
    
