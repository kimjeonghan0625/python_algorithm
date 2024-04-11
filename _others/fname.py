def rmv_vwls(string):
    out = ""
    for e in string:
        if e not in ["a", "e", "i", "o", "u"]:
            out += e
    return out


def my_join(array, string):
    tmp = array[:]
    out = ""
    last = tmp.pop()
    for e in tmp:
        out += e
        out += string
    out += last
    return out


def main():
    l = input().lower().split()
    l[0] = rmv_vwls(l[0])
    out = my_join(l, "_")
    print(out)


if __name__ == "__main__":
    main()
