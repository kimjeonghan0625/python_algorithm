from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 소스코드 구현
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]


print(bfs(0, 0))
