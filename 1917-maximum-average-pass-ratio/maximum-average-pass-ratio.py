class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        #Keep a max-heap of (change, [passed, total])
        #Pop heap and get max-change -> add one to both passed and total and push into max-heap the new value
        #Keep Total Ratio and add max gain to the total ratio
        total_ratio = 0
        for i in range(len(classes)):
            total_ratio += classes[i][0]/classes[i][1]
        
        change_heap = []
        for i in range(len(classes)):
            prev_ratio = classes[i][0]/classes[i][1]
            new_ratio = (classes[i][0]+1)/(classes[i][1]+1)
            change = new_ratio - prev_ratio
            heapq.heappush(change_heap, (-change, [classes[i][0]+1, classes[i][1]+1]))
        
       
        
        # extraStudents -= 1
        while extraStudents:
            max_change, new_values = heapq.heappop(change_heap)
            total_ratio += (-max_change)
            new_ratio = (new_values[0]+1)/(new_values[1]+1)
            prev_ratio = new_values[0]/new_values[1]
            change = new_ratio - prev_ratio
            heapq.heappush(change_heap, (-change, [new_values[0]+1, new_values[1]+1]))
            extraStudents -= 1
        
        return total_ratio/len(classes)


        




        