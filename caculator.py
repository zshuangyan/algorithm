import math
import argparse

args = argparse.ArgumentParser()
args.add_argument("-s", "--start", type=int, help="start index for accumulation")
args.add_argument("-e", "--end", type=int, help="end index for accumulation")
args.add_argument("-b", "--base", type=int, help="base for pow")
args = args.parse_args()


def accumulation(start, end, base):
    total = 0
    for i in range(start, end+1):
        total += math.pow(base, i)
    return total

result = accumulation(**vars(args))
print("%e" % result)
