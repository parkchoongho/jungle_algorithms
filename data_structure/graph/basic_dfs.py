graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

visited_list: list = []


"""
* 재귀로 구현 *
def dfs(vertex: int):
    if vertex not in visited_list:
        visited_list.append(vertex)
        for connected_vertex in graph[vertex]:
            dfs(connected_vertex)

print(visited_list)
"""

"""
* 스택으로 구현 *
def dfs(start_vertex: int):
    visited_list = []
    stack = [start_vertex]

    while stack:
        vertex = stack.pop()

        if vertex not in visited_list:
            visited_list.append(vertex)
            for next_vertex in graph[vertex]:
                stack.append(next_vertex)

    print(visited_list)
"""

# dfs(1)
