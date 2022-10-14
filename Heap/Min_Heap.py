# 힙 삽입
def heap_push(item):
    heap.append(item)
    child = len(heap) - 1
    parent = child // 2

    # 루트노드(parent=0)가 아니고 부모노드가 자식 노드보다 크다면 반복문 실행
    while parent > 0 and heap[parent] > heap[child]:
        # 노드 값 바꿔주고
        heap[parent], heap[child] = heap[child], heap[parent]
        # 원래 부모를 자식으로 만들어주고 부모 재설정
        child = parent
        parent = child // 2


# 힙 삭제 연산
def heap_pop():

    # 루트 노드만 남은 경우 바로 반환
    if len(heap) <= 2:
        return heap.pop()

    item = heap[1]
    heap[1] = heap.pop()
    parent = 1
    child = parent * 2

    # 자식이 하나라도 있으면
    while child < len(heap):
        # 오른쪽 자식이 있고, 왼쪽 자식이 오른쪽 자식보다 크면
        if child + 1 < len(heap) and heap[child] > heap[child + 1]:
            child += 1  # 비교 대상을 오른쪽 자신으로 갱신

        # 부모 노드가 더 크면 최소힙이 아니므로 교환
        if heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            # 원래 자식 노드를 부모노드로 바꿔주고 자식노드 갱신
            parent = child
            child = parent * 2
        else:
            break
    return item


heap = [0]
heap_push(2)
heap_push(5)
heap_push(7)
heap_push(3)
heap_push(4)
heap_push(6)
print(heap)

while len(heap) >= 2:
    print(heap_pop())
