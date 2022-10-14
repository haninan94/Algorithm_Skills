from collections import deque

# bfs 함수
def bfs(v):

    visited[v] = True
    queue = deque([v])
    # 로직
    print(v, end=' ')

    # queue에 정보가 들어있다면 계속 반복
    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if not visited[next_v]:
                queue.appened(next_v)
                print(next_v, end=' ')


n, m = map(int, input().split())  # n: 정점의 개수, m: 간선의 개수
edges = list(map(int, input().split()))  # 간선의 정보
graph = [[] for _ in range(n + 1)]  # 그래프가 1번부터 시작하면 n+1
visited = [False] * (n + 1)

# 인접 리스트
for i in range(0, len(edges), 2):
    v1, v2 = edges[i], edges[i + 1]

    # 양방향 그래프일때
    graph[v1].append(v2)
    graph[v2].append(v1)

# 1번 부터 bfs시작
bfs(1)
