#!/usr/bin/python3

def search_replace(my_list, search, replace):
    list_a = []
    for element in my_list:
        if element == search:
            list_a.appemd(replace)
        else:
            list_a.append(element)
    return list_a
