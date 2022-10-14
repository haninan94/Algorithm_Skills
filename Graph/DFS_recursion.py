# dfs 함수
def dfs(v):
    visited[v] = True

    # 로직
    print(v, end=' ')

    for next_v in graph(v):
        # 다음 정점이 방문처리 되어있지 않다면 다음 정점으로 이동
        if not visited[next_v]:
            dfs(next_v)


n, m = map(int, input().split())  # n:정점 개수, m: 간선 개수

edges = list(map(int, input().split()))  # 간선 정보

graph = [[] for _ in range(n + 1)]  # 정점 번호가 1번부터 시작하면 n+1

visited = [False] * (n + 1)  # 방문 처리 하기 위한 리스트

# 예를 들어 연결 관계가 쌍으로 주어진다면
# ex 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

for i in range(0, len(edges), 2):
    v1, v2 = edges[i], edges[i + 1]
    # 양방향 그래프라면
    graph[v1].append(v2)
    graph[v2].append(v1)

# 1번부터 깊이 우선 탐색
dfs(1)
