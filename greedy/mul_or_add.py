# success (12:37 left)
input_string = input()
result = int(input_string[0])
for i in range(1, len(input_string)):
    num = int(input_string[i])
    if result < 2 or num < 2:
        result += num
    else:
        result *= num

print(result)
