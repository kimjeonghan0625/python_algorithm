my_list = [11, 3, 23, 7]
""" 아이템 찾기에 걸리는 시간복잡도는 O(N) -> 선형 검색 """


def search_by_item(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return -1


print(search_by_item(my_list, 7))

""" 아이템 찾기에 걸리는 시간복잡도는 O(1) -> 한 방에 찾기 때문 """


def search_by_index(list, index):
    return list[index]


print(search_by_index(my_list, 3))
