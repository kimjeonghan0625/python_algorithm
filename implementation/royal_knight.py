xarr=[0,"a","b","c","d","e","f","g","h"]
tmp=input()
x=xarr.index(tmp[0])
y=int(tmp[1])
dx=[-1,1,2,2,-2,-2,1,-1]
dy=[-2,-2,1,-1,1,-1,2,2]
count=0
for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<1 or ny<1 or nx >8 or ny > 8:
        continue
    count+=1
print(count)