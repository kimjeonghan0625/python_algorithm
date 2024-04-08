INF = int(1e9)
v = int(input())
e = int(input())
d = [[INF] * (v + 1) for _ in range(v + 1)]
for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i == j:
            d[i][j] = 0
for _ in range(e):
    a, b, c = map(int, input().split())
    d[a][b] = c
for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            d[a][b] = min(d[a][b], d[a][k] + d[k][b])
for a in range(1, v + 1):
    for b in range(1, v + 1):
        if d[a][b] == INF:
            print("INF", end=" ")
        else:
            print(d[a][b], end=" ")
    print()
