def mk_lower_alpha_list(char_arr):
    lower_alpha_arr = []
    for e in char_arr:
        if 65 <= ord(e) <= 90: 
            lower_alpha_arr.append(chr(ord(e) + 32))
        elif 97 <= ord(e) <= 122:
            lower_alpha_arr.append(e)
    return lower_alpha_arr


def mk_cweight_dict(str_arr):
    tmp_dict = {}
    for e in str_arr:
        tmp_dict[e] = str_arr.count(e)
    for k, v in tmp_dict.items():
        if k in ["w", "y"]:
            tmp_dict[k] = 1.5**v
        elif k in ["a", "e", "i", "o", "u"]:
            tmp_dict[k] = 2.0**v
        else:
            tmp_dict[k] = 1.2**v
    return tmp_dict


if __name__ == "__main__":
    char_list = list(input())
    lower_alpha_list = mk_lower_alpha_list(char_list)
    cweight_dict = mk_cweight_dict(lower_alpha_list)
    heavy_c_relative_weight = max(cweight_dict.values()) / sum(cweight_dict.values()) * 100
    print(f"{heavy_c_relative_weight:.3f}")
