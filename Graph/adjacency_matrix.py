# 그래프의 표현
# 1) 인접 행렬 (Adjacent Matrix)

n, m = map(int, input().split())  # 정점, 간선 개수
graph = [[0] * n for _ in range(n)]  # n x n의 인접 행렬 초기화

# 간선의 개수만큼 반복하면서 인접 행렬에 표시
for _ in range(m):
    v1, v2 = map(int, input().split())  # 인접한 정점 2개
    graph[v1][v2] = 1
    graph[v2][v1] = 1

# 인접 행렬 출력
for line in graph:
    print(*line)
