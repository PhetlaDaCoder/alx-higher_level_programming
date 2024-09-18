#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    my_tuple = ()
    1_tuple = tuple_a + (0, 0)
    2_tuple = tuple_b + (0, 0)
    my_tuple = 1_tuple[0] + 2_tuple[0], 1_tuple[1] + 2_tuple[1]
    return my_tuple
