def interchange_first_and_last_element_of_list(list):
    temp = list[0]
    list[0] = list[-1]
    list[-1] = temp
    return list




print(interchange_first_and_last_element_of_list([12, 35, 9, 56, 24]))
