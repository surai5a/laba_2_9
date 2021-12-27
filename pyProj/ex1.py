#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def recursion(n):
    if n == 1:
        return 1

    return n + recursion(n - 1)


if __name__ == '__main__':
    print(f"Recursion: {recursion(5)}")

    n = 0
    k = 5
    for i in range(1, k + 1):

        n += i

    print(f"'for': {n}")
