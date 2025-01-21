class RandomizedCollection:

    def __init__(self):
        self.indexMap = {}
        self.array = []

    def insert(self, val: int) -> bool:
        index_to_append = len(self.array)
        self.array.append(val)
        if val not in self.indexMap:
            self.indexMap[val] = set()
            self.indexMap[val].add(index_to_append)
            return True
        else:
            self.indexMap[val].add(index_to_append)
            return False
    
    #Remove an occurence of val
    def remove(self, val: int) -> bool:
        if val not in self.indexMap:
            return False
            
        val_index = self.indexMap[val].pop()
        curr_last_element = self.array[-1]
        if val_index != (len(self.array)) - 1:
            self.array[val_index] = curr_last_element
            self.indexMap[curr_last_element].remove(len(self.array) - 1)
            self.indexMap[curr_last_element].add(val_index)
    
        self.array.pop()
        
        if len(self.indexMap[val]) == 0:
            del self.indexMap[val]
        
        return True  

    def getRandom(self) -> int:
        val = random.choice(self.array)
        return val
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()