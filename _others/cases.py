a = list(input())
b = list(input())
ai = 0
bi = 0
ap = 0
bp = 0
for i, e in enumerate(a):
    if e == "X":
        ai = i
        a[i] = "0"
for i, e in enumerate(b):
    if e == "X":
        bi = i
        b[i] = "0"
basea = int("".join(a))
baseb = int("".join(b))
ap = len(a) - ai - 1
bp = len(b) - bi - 1
count = 0


def f(i):
    global count
    for j in range(10):
        if i == j:
            continue
        if basea + 10**ap * i > baseb + 10**bp * j:
            count += 1


for i in range(10):
    f(i)

print(count)
