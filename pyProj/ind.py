#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def all_perms(arr):
    if len(arr) == 1:
        return [arr]
    else:
        a = arr[0]
        p = all_perms(arr[1:])
        r = []
        for pp in p:
            for i in range(len(pp)):
                tmp = pp[0:i] + [a] + pp[i:]
                r.append(tmp)
            r.append(pp + [a])
        return r


if __name__ == '__main__':
    print(all_perms([1, 2]))
