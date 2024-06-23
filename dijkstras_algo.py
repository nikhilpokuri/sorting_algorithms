import heapq

def dijkstras(start):
    pq = [(0, start)]
    distances = {vertex: float("inf") for vertex in graph }
    distances[start] = 0
    visited = set()
    while pq:
        curr_dis, curr_ver = heapq.heappop(pq)
        if curr_ver in visited:
            continue
        
        visited.add(curr_ver)

        for adj_ver, adj_dis in graph[curr_ver].items():
            new_dis = curr_dis + adj_dis

            if new_dis < distances[adj_ver]:
                distances[adj_ver] = new_dis
                heapq.heappush(pq, (new_dis, adj_ver))
    return distances
graph = {
    "A" : {"B": 3, "E": 20},
    "B" : {"C": 2, "A": 3},
    "C" : {"D":1, "B": 2},
    "D" : {"E": 4, "C": 1},
    "E" : {"A": 20, "D": 4}
}
print(dijkstras("A"))
