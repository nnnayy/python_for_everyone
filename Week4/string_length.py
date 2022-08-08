#!/usr/bin/python
# -*- coding: latin-1 -*-

def count_word(text, word):
    f = open("text.txt", 'w')

    if word in text:
        cnt = text.count(word)
        print(cnt)

    f.write(text)
    f.close()

text = """나의 생은 미친듯이 사랑을 찾아 헤매었으나\n단 한번도 스스로를 사랑하지 않았노라
"""
count_word(text, "사랑")