def q_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    q_sort(array, start, right - 1)
    q_sort(array, right + 1, end)


def q_sort2(array):
    if len(array) <= 1:
        return array
    p = array[0]
    remain = array[1:]
    left = [x for x in remain if x <= p]
    right = [x for x in remain if x > p]
    return q_sort2(left) + [p] + q_sort2(right)


# n = int(input())
array = list(map(int, input().split()))
a=q_sort2(array)
print(a)
# for e in array:
#     print(e, end=" ")
# print()
