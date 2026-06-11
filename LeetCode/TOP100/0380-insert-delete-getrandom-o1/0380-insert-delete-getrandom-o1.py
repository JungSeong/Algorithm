import random

class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.d = {}
    def insert(self, val: int) -> bool:
        if val not in self.d.keys() :
            idx = len(self.arr)
            self.d[val] = idx
            self.arr.append(val)
            return True
        else :
            return False
    def remove(self, val: int) -> bool:
        if val in self.d.keys() :
            idx = self.d[val]
            last = self.arr[-1]
            self.d[last] = idx
            del self.d[val]
            self.arr[idx] = last
            self.arr.pop()
            return True
        else :
            return False
    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()