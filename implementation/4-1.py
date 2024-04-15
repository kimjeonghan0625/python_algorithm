n = int(input())
arr=input().split()
x,y=1,1
d=["L","R","U","D"]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
for e in arr:
    for di,de in enumerate(d):
        if de == e:
            nx=x+dx[di]
            ny=y+dy[di]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x,y=nx,ny
print(x, y)