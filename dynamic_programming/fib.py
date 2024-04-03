counter = 0


def fib_div_and_conq(num: int):
    global counter
    counter += 1
    if num == 0 or num == 1:
        return num
    return fib_div_and_conq(num - 1) + fib_div_and_conq(num - 2)


memo = [None] * 100


def fib_memo(num: int):
    global counter
    counter += 1
    if memo[num] is not None:
        return memo[num]
    if num == 0 or num == 1:
        return num
    memo[num] = fib_memo(num - 1) + fib_memo(num - 2)
    return memo[num]


def fib_iter(num: int):
    dp = [0, 1]
    global counter
    for i in range(2, num + 1):
        counter += 1
        next_fib = dp[i - 1] + dp[i - 2]
        dp.append(next_fib)
    return dp[num]


res = fib_iter(35)
print(f"counter num is {counter} and res is {res}")
