# 균형잡힌 세상 - 실버4
# https://www.acmicpc.net/problem/4949

import sys


sys.stdin = open("input.txt")


def solution():
    while True:
        texts = input()
        # 종료조건
        if texts == ".":
            return

        # (, [ == 0, 1
        stack = []
        switch = False
        for text in texts:
            if text == "(":
                stack.append(0)
            elif text == "[":
                stack.append(1)
            elif text == ")":
                if stack and stack[-1] == 0:
                    stack.pop()
                else:
                    print("no")
                    switch = True
                    break
            elif text == "]":
                if stack and stack[-1] == 1:
                    stack.pop()
                else:
                    switch = True
                    print("no")
                    break
        if switch:
            continue
        if not stack:
            print("yes")
        else:
            print("no")


solution()
