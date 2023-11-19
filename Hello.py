from io import TextIOWrapper
import string
import time
import FunctionTimer

@FunctionTimer.TimeFunction
def main():
    l = []
    for i in range(100000000):
        l.append(i * i %3)


main()
