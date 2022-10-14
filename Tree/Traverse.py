# 루트 노드 찾기
def find_root(v):
    # 정점을 다 확인해서 정점노드의 부모노드 정보가 0이라면 그것이 루트노드
    for node in range(1, v + 1):
        if tree[node][2] == 0:
            return node


# 전위 순회
def pre_order(node):
    if node != 0:
        print(node, end=' ')
        pre_order(tree[node][0])
        pre_order(tree[node][1])


# 중위 순회
def in_order(node):
    if node != 0:
        in_order(tree[node][0])
        print(node, end=' ')
        in_order(tree[node][0])


# 후위 순회
def post_order(node):
    if node != 0:
        post_order(tree[node][0])
        post_order(tree[node][1])
        print(node, end=' ')


v = int(input())  # 정점의 개수
tree = [[0] * 3 for _ in range(v + 1)]  # 0이 3개인 이유는 좌측 자식노드, 우측 자식노드, 뿌리 노드
edges = list(map(int, input().split()))

# 이진 트리 구현
for i in range(0, len(edges), 2):
    parent, child = edges[i], edges[i + 1]

    # 부모 노드번재의 tree 첫번째 원소(좌측 자식노드)가 비어있다면 좌측에 저장
    if tree[parent][0] == 0:
        tree[parent][0] == child
    # 좌측 자식노드 차있으면 우측에 저장
    else:
        tree[parent][1] == child
    # 자식노드의 세번째 원소(부모 원소를 나타내는 자리)에 부모 노드 정보 저장
    tree[child][2] = parent

root = find_root(v)

pre_oreder(root)

in_order(root)

post_order(root)
