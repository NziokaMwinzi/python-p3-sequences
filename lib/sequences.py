#!/usr/bin/env python3

def print_fibonacci(length):
    my_list=[]
    if(length == 0):
        print(my_list)
    elif(length == 1):
        my_list.append(0)
        print(my_list)
    elif(length == 2):
        my_list=[0]
        my_list.insert(1,1)
        print(my_list)
    else:
        my_list=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        print(my_list)
