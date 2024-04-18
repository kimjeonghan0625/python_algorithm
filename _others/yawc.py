def mk_loweralpha_charlist(line):
    charlist = list(line)
    loweralpha_charlist = []
    for e in charlist:
        if e.isalpha():
            loweralpha_charlist.append(e.lower())
    return loweralpha_charlist


def mk_cweight_set(charlist):
    ws = set()
    for e in charlist:
        if e in "aeiou":
            ws.add((e, 2.0 * charlist.count(e)))
        elif e in "wy":
            ws.add((e, 1.5 * charlist.count(e)))
        else:
            ws.add((e, 1.0 * charlist.count(e)))
    return ws


if __name__ == "__main__":
    l = input()
    lacl = mk_loweralpha_charlist(l)

    def second_item_of_element(tp):
        return tp[1]

    sorted_cweight_list = sorted(
        list(mk_cweight_set(lacl)), key=second_item_of_element, reverse=True
    )
    heaviest = sorted_cweight_list[0][1]
    cweight_sum = sum(map(second_item_of_element, sorted_cweight_list))
    print(f"{heaviest/cweight_sum*100:.3f}")
