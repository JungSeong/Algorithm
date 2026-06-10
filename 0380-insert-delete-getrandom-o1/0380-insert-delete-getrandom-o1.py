import random

class RandomizedSet:
    def __init__(self):
        self.s = []
        self.d = {}
    def insert(self, val: int) -> bool:
        if val not in self.d.keys() :
            idx = len(self.s)
            self.d[val] = idx
            self.s.append(val)
            return True
        else :
            return False
    def remove(self, val: int) -> bool:
        if val in self.d.keys() :
            idx = self.d[val]
            v = self.s[-1]            
            self.s[idx] = v
            self.d[v] = idx

            self.s.pop()
            del self.d[val]
            return True
        else :
            return False
    def getRandom(self) -> int:
        return random.choice(self.s)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()