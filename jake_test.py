def hex_to_dec(hex_str):
    list1 = []
    list1[:0] = hex_str
    multi = 1
    ind = 0
    list2 = []
    for i in list1:
        if i == "a":
            list2.insert(0, 10)
        elif i == "b":
            list2.insert(0, 11)
        elif i == "c":
            list2.insert(0, 12)
        elif i == "d":
            list2.insert(0, 13)
        elif i == "e":
            list2.insert(0, 14)
        elif i == "f":
            list2.insert(0, 15)
        else:
            list2.insert(0, int(i))

    result_list = []
    for power, i in enumerate(list2):
        place_value = 16**power
        result_list.append(place_value * i)

    return sum(result_list)


hex_num = "3d1f"
# A = 10
# B = 11
# C = 12
# D = 13
# E = 14
# F = 15
print(hex_to_dec(hex_num))
