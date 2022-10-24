#!/usr/bin/python3
""" Module includes a `MyInt` class"""


class MyInt(int):
    """`MyInt` has == and != operators inverted"""
    def __eq__(self, other):
        return self - other != 0

    def __ne__(self, other):
        return self - other == 0
