#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """ prints an integer.

    Prototype: def safe_print_integer_err(value):
    value can be any type (integer, string, etc.)
    The integer should be printed followed by a new line
    Returns True if value has been correctly printed (it means the value is an integer)
    Otherwise, returns False and prints in stderr the error precede by Exception:
    You have to use try: / except:
    You have to use "{:d}".format() to print as integer
    You are not allowed to use type()
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
