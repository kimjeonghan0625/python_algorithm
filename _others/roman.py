def calc_r(r, n=0):
    new = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}[r[-1]]
    nsum = n + new if new >= n else n - new
    return nsum if len(r) == 1 else calc_r(r[:-1], nsum)


if __name__ == "__main__":
    print(calc_r(input()))

# s=input()
# n=len(s)
# dp={"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
# for i in range(1, n):
#     new, old = dp[s[-i-1]],dp[s[-i:]]
#     dp[s[-i-1:]] = old + new if new >= old else old - new
# print(dp[s])
