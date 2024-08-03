def interchange_two_elements_in_the_list(list, pos1, pos2):
    list[pos1 - 1] , list[pos2 - 1] = list[pos2 - 1] , list[pos1 - 1]
    return list

print(interchange_two_elements_in_the_list([23, 65, 19, 90], 1, 3))