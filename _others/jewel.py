def f(arr):
    d={}
    for e in arr:
        if e in d:
            continue
        d[e]=arr.count(e)
    m=max(d.values())
    print(m)
    print(f"{m/len(arr):.2f}")

if __name__=="__main__":
    l=input().split()
    f(l)

    