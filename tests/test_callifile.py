from printind.printind_function import printi
from callifile.callifile import callifile
import sys


def f_1():
    printi("f1")


def f_2():
    printi("f2")


def test_callifile():
    # careful: need the pattern_to_call here, otherwise recursive call!
    callifile(module=sys.modules[__name__], verbose=True, pattern_to_call="f_*")


if __name__ == '__main__':
    callifile(module=sys.modules[__name__], verbose=True)
