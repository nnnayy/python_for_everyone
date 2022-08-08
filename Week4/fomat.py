#!/usr/bin/python
# -*- coding: latin-1 -*-
# 3자리마다 , 를 찍어서 구분해 주는 프로그램
# f"{숫자:,}"

def make_comma(num) :
    num = int(input("숫자를 입력하세요 : "))
    print(format(num, ','))

make_comma(1000000)