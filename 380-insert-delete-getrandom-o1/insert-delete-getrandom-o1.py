class RandomizedSet:

    def __init__(self):
        self.values = []
        self.dict = {}
        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False

        self.dict[val] = len(self.values)
        self.values.append(val)

        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        
        index = self.dict[val]
        last_element = self.values[-1]
        self.dict[last_element] = index
        self.values[-1], self.values[index] = self.values[index], self.values[-1]

        self.values.pop()
        del self.dict[val]
        return True
        

    def getRandom(self) -> int:

        return choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()