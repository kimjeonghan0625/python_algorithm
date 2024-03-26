# L: 왼 R: 오 U: 위 L: 왼
n = int(input())
data = input().split()
result = [1, 1]
x = [0, -1, 0, 1]  # 좌 위 우 아
y = [-1, 0, 1, 0]
dir = {"L": 0, "U": 1, "R": 2, "D": 3}
for elem in data:
    result[0] += x[dir[elem]]
    result[1] += y[dir[elem]]
    if result[0] < 1 or result[0] > n or result[1] < 1 or result[1] > n:
        result[0] -= x[dir[elem]]
        result[1] -= y[dir[elem]]
print(" ".join(list(map(str, result))))
