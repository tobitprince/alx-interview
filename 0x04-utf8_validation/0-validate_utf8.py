#!/usr/bin/python3
"""Module for validUTF8 function."""


def validutf8(data):
    """Return true if data is a valid UTF-8 encoding, else return false."""
    try:
        bytes(data).decode('utf-8')
        return True
    except (UnicodeDecodeError, ValueError, TypeError):
        return False
