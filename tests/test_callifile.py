from printind.printind_function import printi
from callifile.callifile_functions import callifile
import sys


def f_1():
    printi("f1")


def f_2():
    printi("f2")


def test_callifile():
    callifile(module=sys.modules[__name__], verbose=True, pattern_to_call="f_*")


def test_callifile_full_auto():
    callifile()


if __name__ == '__main__':
    callifile()
