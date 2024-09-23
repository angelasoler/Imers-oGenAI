#!/usr/bin/env python3.10

from time import sleep, time
from decimal import Decimal

def ft_progress(lst):
    start = time()
    for l in lst:
        elapsed = time() - start
        perc = round((l + 1) / len(lst) * 100)
        eta = 0.0
        if perc != 0:
            eta = round(100 / (perc / elapsed), 2)
        bar = "[" + "=" * round(perc/10) + ">" + " " * round(10 - perc/10) + "]"
        print(f"\rETA: {eta:{5}}s [{perc:{3}}%]{bar} {l + 1}/{len(lst)} | elapsed time {elapsed:.2f}s", end="")
        yield l
    print("\n...", end="")

a_list = range(1000)
ret = 0
for elem in ft_progress(a_list):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)