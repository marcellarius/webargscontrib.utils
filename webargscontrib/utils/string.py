__author__ = 'sam'


def lowercase(value):
    try:
        return value.lower()
    except (AttributeError, ValueError):
        return value


def strip(value):
    try:
        return value.strip()
    except (AttributeError, ValueError):
        return value


