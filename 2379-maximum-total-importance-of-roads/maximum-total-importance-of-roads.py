import heapq as hq
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        nodes = {}
        for i in range(n):
            nodes[i] = 0
        
        for i in range(len(roads)):
            nodes[roads[i][0]] = nodes.get(roads[i][0], 0) + 1
            nodes[roads[i][1]] = nodes.get(roads[i][1], 0) + 1
        

        print(nodes)
        nodes = {k: v for k, v in sorted(nodes.items(), key=lambda item: item[1])}
        print(nodes)

        i = 1
        for k, v in nodes.items():
            nodes[k] = i
            i = i + 1
        
        print(nodes)
        # # List to hold values from dictionary
        # heap_dict=[]
 
        # # extract the values from dictionary
        # for i in nodes.values():
        #     heap_dict.append(i)
     
        # # heapify the values
        # hq.heapify(heap_dict)   
        # print("Values of the dict after heapification :",heap_dict)
 
        # # list to hold final heapified dictionary
        # new_dict=[]

        # # mapping and reconstructing final dictionary
        # for i in range(0,len(heap_dict)):
     
        #     # Iterating the oringinal dictionary
        #     for k,v in nodes.items():
            
        #         if v==heap_dict[i] and (k,v) not in new_dict:
        #             new_dict.append((k,v))
        # i = 1
        # imp_arr = {}
        # while new_dict:
        #     item = hq.heappop(new_dict)
        #     value = i
        #     node = item[0]
        #     imp_arr[node] = value
        #     i = i+1 

        # print("Final dictionary :",new_dict)

        importance = 0
        
        for i in range(len(roads)):
            a = roads[i][0]
            b = roads[i][1]

            road_value = nodes[a] + nodes[b]
            importance += road_value


        return importance