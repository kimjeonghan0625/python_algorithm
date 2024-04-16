def hamming(s1, s2):
    # h = 0
    # for c1, c2 in zip(s1, s2):
    #     if c1 != c2:
    #         h += 1
    return len([1 for c1, c2 in zip(s1, s2) if c1 != c2])


def main():
    l1 = input().lower()
    l2 = input().lower()
    print(hamming(l1, l2))


if __name__ == "__main__":
    main()
