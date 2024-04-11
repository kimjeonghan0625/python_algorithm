def word_capitalize(word):
    return word[0].upper() + word[1:]


def my_capitalize(array):
    ol = []
    for e in array:
        if e in ["i", "you", "we", "she", "he", "they"]:
            ol.append(word_capitalize(e))
            continue
        if len(e) >= 5:
            ol.append(word_capitalize(e))
            continue
        ol.append(e)
    return ol


def main():
    sl = input().split()
    ol = my_capitalize(sl)

    print(" ".join(ol))


if __name__ == "__main__":
    main()
