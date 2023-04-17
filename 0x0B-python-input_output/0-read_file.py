#!/usr/bin/python3
"""Function that reads and prints to stdout"""


def read_file(filename=""):
    """function that reads and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
