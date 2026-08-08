from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.od = OrderedDict()
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key in self.od.keys() :
            self.od.move_to_end(key)
            return self.od[key]
        else :
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.od.keys() :
            self.od[key] = value
            self.od.move_to_end(key)
        else :
            if len(self.od) == self.capacity :
                self.od.popitem(False)
            self.od[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)