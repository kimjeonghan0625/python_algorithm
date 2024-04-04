def my_split(string):
    start = 0
    split_list = list()
    for i in range(len(string)):
        if string[i].isspace():
            split_list.append(string[start:i])
            start = i + 1
    split_list.append(string[start : len(string)])  # add last num
    return split_list

def main():
    given_diameter = int(input())
    given_sequence = list(map(int, my_split(input())))
    temp = list()
    temp.append(given_sequence[0])
    res = len(given_sequence)
    for i in range(1, len(given_sequence)):
        temp.append(given_sequence[i])
        if given_diameter < max(temp) - min(temp):
            res = i
            break

    print(res)

if __name__ == "__main__":
    main()
