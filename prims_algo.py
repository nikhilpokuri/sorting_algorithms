import heapq

def prims(start):
    mst = []
    visited = set()
    pq = [(0, start, None)]

    while pq:
        curr_dis, curr_ver, prev_ver = heapq.heappop(pq)
        if curr_ver not in visited:
            visited.add(curr_ver)
            mst.append((curr_dis, curr_ver, prev_ver))

        for adj_ver, adj_dis in graph[curr_ver].items():
            if adj_ver not in visited:
                heapq.heappush(pq, (adj_dis, adj_ver, curr_ver))
    
    # not printing from None to A, as it is starting node
    for distance, curr_node, prev_node in mst[1:]:
        print(f"{prev_node} -> {curr_node} : {distance}")

graph = {
    "A": {"B": 2, "D": 1},
    "B": {"A": 2, "C": 3, "D": 1, "E": 5},
    "C": {"B": 3, "E": 1},
    "D": {"A": 1, "B": 1, "E": 4},
    "E": {"B": 5, "C": 1, "D": 4}
}

prims("A")