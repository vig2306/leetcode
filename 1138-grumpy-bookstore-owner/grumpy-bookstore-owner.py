class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
    
        max_val = 0
        total_val = 0
        for i in range(len(customers)):
            if i < minutes:
                total_val = total_val + customers[i]
            else:
                total_val = total_val + customers[i]*(not grumpy[i])
        
        max_val = total_val

        for i in range(minutes, len(customers)):
            start = i - minutes + 1
            if grumpy[start-1] == 0:
                if grumpy[i] != 0:
                    total_val = total_val + customers[i]
            
            else:
                if grumpy[i] != 0:
                    total_val = total_val - customers[start-1] + customers[i]
                else:
                    total_val = total_val - customers[start-1]
            
            max_val = max(total_val, max_val)
        
        return max_val
            



       # max_val = 0
        # total_val = 0

        # for i in range(len(customers)):
        #     total_val = total_val + customers[i]*(not grumpy[i])
        
        # max_val = total_val
        
        # for i in range(len(customers)):
        #     start = i-minutes+1
        #     end = i
        #     # if start < 0:
        #     #     curr_val = customers[i]*(not grumpy[i])
        #     #     total_val = total_val + curr_val
        #     if start == 0:
        #         window_sum = sum(customers[start:end+1])
        #         window_sum_remove = 0
        #         for j in range(start,end+1):
        #             window_sum_remove = window_sum_remove + customers[j]*(not grumpy[j])
                
        #         total_val = total_val + window_sum - window_sum_remove

        #     elif start > 0:
        #         total_val = total_val + customers[i] - customers[start-1]*grumpy[start-1]

        #     max_val = max(max_val, total_val)
        
        # return max_val 
        