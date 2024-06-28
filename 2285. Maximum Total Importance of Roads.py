from collections import defaultdict
from typing import List

class Solution:
    '''
    Approach: Using hashmap
    get in-degrees
    sort based on that
    add weights
    traverse roads and calculate total


    # I: 5 4 3 2 1
    
    # R: 4 3 2 2 1
    # C: 2 1 3 0 4

    Time: O(len(roads)), i.e # of edges, could be N ^ 2 in worst case. And sorting 
    Space: O(N)
    '''
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        city_road = defaultdict(int)
        ans = 0

        for x, y in roads:
            city_road[x] += 1
            city_road[y] += 1

        city_road = dict(sorted(city_road.items(), key = lambda x : x[1], reverse=True))

        city_road_imp = defaultdict(list)
        for k, v in city_road.items():
            city_road_imp[k].append(v)
            city_road_imp[k].append(n)
            n -= 1
        
        for x, y in roads:
            ans += city_road_imp[x][1] + city_road_imp[y][1]

        return ans

    '''
    Approach: using just array and multiplication of in_degree and weight of node
    Time: O(len(roads)), i.e # of edges, could be N ^ 2 in worst case. And sorting 
    Space: O(N)
    '''
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        in_degree = [0 for _ in range(n)]

        for a, b in roads:
            in_degree[a] += 1
            in_degree[b] += 1

        in_degree.sort()

        for i in range(n):
            ans += in_degree[i] * (i + 1)

        return ans