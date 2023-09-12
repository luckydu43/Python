# https://www.codingame.com/ide/puzzle/temperatures
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
result = 5530
for i in input().split():
    if abs(int(i)) < abs(int(result)):
        result = int(i)
    if abs(int(i)) == abs(int(result)):
        if int(i) + int(result) >= 0:
            result = abs(int(i))
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
if result == 5530:
    result = 0
print(result)
