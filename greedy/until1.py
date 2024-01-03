n, k  = map(int, input().split())
# count = 0

# while n != 1:
#     if n % k == 0:
#         n = n / k
#         count += 1
#     else:
#         n = n - 1
#         count += 1
# print(count)

result = 0

while True:
    # 나누어 떨어지는 수가 될 떄까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k: # 제수가 피제수보다 크면 반복문을 빠져나감
        break
    result += 1 # 연산횟수를 1 높임
    n //= k # n을 k로 나눈 몫을 n에 대입함

# 마지막으로 남은 수에 대하여 1씩 빼기
result += n - 1
print(result)