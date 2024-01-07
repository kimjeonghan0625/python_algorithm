from typing import Any, Sequence


# 배열 맨 앞부터 순서대로 원소를 스캔하는 선형 검색은
# 원소의 값이 정렬되지 않은 배열에서 검색할 때 사용하는 유일한 방법
def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색"""
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1


if __name__ == "__main__":
    num = int(input("원소 수를 입력하세요: "))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    ky = int(input("검색할 값을 입력하세요.: "))
    idx = seq_search(x, ky)
    if idx == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else:
        print(f"검색값은 x[{idx}]에 있습니다.")
