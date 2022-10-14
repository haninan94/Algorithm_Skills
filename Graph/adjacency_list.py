n, m = map(int, input().split())  # n: 정점, m: 간선의 개수

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())

    # 양방향 일때
    graph[v1].append(v2)
    graph[v2].append(v1)

    # 단방향 일때 v1에서 v2로 방향성을 가진다면
    # graph[v1].append(v2)

for line in graph:
    print(*line)
