#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

def count_v1():

    myStr = 'apple orange witch beach art young'
    myList = myStr.split(' ')
    a = ('i','o','e','y','u','a')
    for elem in myList:
        print (elem)
    print()

    for elem in range (len(myList)):
        b = list(myList[elem])
        for i in range(1):
            if b[0] in a:
                print (myList[elem])


def count_v2():
    myStr = 'A lot of, relatives c are here for: z the wedding party. Were v very busy'
    for p in string.punctuation:
        if p in myStr:
            myStr = myStr.replace(p, "")

    myList = myStr.split(' ')


    print(myList)


count_v2()