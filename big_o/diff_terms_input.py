def print_items(a, b):
    for i in range(a):
        print(a)
    for j in range(b):
        print(b)


print_items(10)

""" print_items는 O(a + b)의 시간복잡도를 갖는다"""


def print_items2(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)


""" print_items2는 O(a * b)의 시간복잡도를 갖는다"""
