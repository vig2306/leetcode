class Solution:
    def sieve(self, N):
        prime = [1]*(N+1)
        prime[0] = 0
        prime[1] = 0
        MaxRange = int(N**0.5)+1
        for i in range(2, MaxRange):
            if prime[i] == 1:
                for j in range(i*i, N+1,i):
                    prime[j] = 0

        return prime
    
    def findPrime(self, curr_no, next_no, prime_arr):
        first_no = 0
        p = curr_no - next_no
        for i in range(p+1, curr_no):
            if prime_arr[i] == 1:
                first_no = i
                break
        return first_no
    
    def is_Sorted(self, arr):
        flag = 0
        for i in range(1,len(arr)):
            if arr[i] <= arr[i-1]:
                flag = 1
        
        return True if flag == 0 else False
                
    def primeSubOperation(self, nums: List[int]) -> bool:
        if self.is_Sorted(nums) == True:
            return True
        max_no = max(nums)
        prime_arr = self.sieve(max_no)
        # print(prime_arr)
        values = nums.copy()
        for i in range(len(values)-2,-1,-1):
            if values[i] >= values[i+1]:
                subtract = self.findPrime(values[i], values[i+1], prime_arr)
                values[i] = values[i] - subtract  

        print(values)          
                
        return self.is_Sorted(values)