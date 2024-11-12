class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        result = []
        items.sort(key=lambda x: x[1], reverse= True)
        for i in range(len(queries)):
            max_beauty = 0
            for price, beauty in items:
                if beauty >= max_beauty:
                    if price <= queries[i]: 
                        max_beauty = max(max_beauty, beauty)
                else:
                    break
            
            result.append(max_beauty)
        
        return result
        