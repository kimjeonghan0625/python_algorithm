import time

# 거듭제곱을 얻는 함수를 분할정복 알고리즘으로 구현해보자.


def power1(base, power):
    if power == 0:
        return 1
    return power1(base, power - 1) * base


def power2(base, power):
    if power == 0:
        return 1
    if power % 2 == 0:
        return power2(base, power // 2) * power2(base, power // 2)
    else:
        return power2(base, power // 2) * power2(base, power // 2) * base


def power3(base, power):
    if power == 0:
        return 1
    x: int = power2(base, power // 2)
    if power % 2 == 0:
        return x * x
    else:
        return x * x * base


# 성능비교
def check_time(f, *args):
    if len(args) != 2:
        print("Error: 두 개의 매개변수가 추가로 필요함")
        return
    start_time = time.time()
    f(*args)
    end_time = time.time()
    result = end_time - start_time
    print(f"N이 {args[1]}일 때 {f} 함수의 수행시간은 {result}입니다")
    return result

def compare_three(a, b, c):
    ta = a["time"]
    tb = b["time"]
    tc = c["time"]
    if ta > tb:
        if tc > ta:
            return [c, a, b]        
        if tb > tc:
            return [a, b, c]
        else:
            return [a, c, b]
    else:
        if tc > tb:
            return [c, b, a]    
        if tc > ta:
            return [b, c, a]
        else:
            return [b, a, c]
        

# x = check_time(power1, 2, 100)
# check_time(power2, 2, 100)
# a = check_time(power3, 2, 100)
# print()

a = {"name": "power1", "time":check_time(power1, 2, 100) }
b = {"name": "power2", "time":check_time(power2, 2, 100) }
c = {"name": "power3", "time":check_time(power3, 2, 100) }

print(compare_three(a, b, c))
