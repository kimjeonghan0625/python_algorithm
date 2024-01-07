from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 그래프 초기화까지 함.
# 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서 최단 거리가
# 정확히 K인 도시의 번호를 출력해야 함.
# 구현 계획 - 어떤 도시 X에서 도달할 수 있는 모든 도시에 대한 최단 거리 리스트를 구함
# 그 리스트를 순회하면서 K인 도시를 검사하여 출력함

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)
