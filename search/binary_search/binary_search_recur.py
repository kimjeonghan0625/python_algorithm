def bs(A, a, b, k):
    if a > b: return -1
    m = (a + b) // 2
    if A[m] == k:
        return m
    elif A[m] > k:
        return bs(A, a, m-1, k)
    elif A[m] < k:
        return bs(A, m+1, b, k)

A = [2, 3, 9, 10, 17, 28, 31, 45]
print(bs(A, 0, len(A)-1, 40)) # -1
print(bs(A, 0, len(A)-1, 31)) # 6