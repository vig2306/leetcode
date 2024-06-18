class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        n = len(difficulty)
        m = len(worker)

        if max(worker) < min(difficulty):
            return 0
        
        dif = []
        for i in range(n):
            new_tup = (difficulty[i], profit[i])
            dif.append(new_tup)
        
        dif.sort()
        worker.sort()
        
        # max_profit = 0
        i = 0
        # curr_profit = 0
        # last_ind = -1
        max_ind = -1
        total_profit = 0
        for j in range(m):
            if max_ind == -1:
                max_profit = 0
            else:
                max_profit = dif[max_ind][1]
            while i < n:

                if dif[i][0] <= worker[j]:
                    curr_profit = dif[i][1]
                    if curr_profit >= max_profit:
                        max_profit = curr_profit
                        max_ind = i
                    i+=1
                else:
                    total_profit += max_profit
                    if max_ind > -1:
                        i = max_ind
                    break
            
            if i == n:
                total_profit += max_profit
                i = n-1

        
        return total_profit

            


        