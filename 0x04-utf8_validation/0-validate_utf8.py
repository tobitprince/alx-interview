#!/usr/bin/python3
"""Module for validUTF8 function."""


def validUTF8(data):
    """ Return: True if data is a valid UTF-8 encoding, else return False
    """
    try:
        bytes(data).decode('utf-8')
        return True
    except Exception:
        return False
