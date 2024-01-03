import time

start = time.time()
n = int(input())

result = 0
while n >= 0:
    if n == 3 or n == 13 or n == 23:
        result += 60 * 60
        n -= 1
    else:
        result += (60 * 60) - (5 * 9 * 5 * 9)
        n -= 1

print(result)
end = time.time()
print(f"{end - start:.5f} sec")
