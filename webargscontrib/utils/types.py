__author__ = 'sam'

from .string import lowercase

def boolean(value):
    return lowercase(value) in {True, "true", "t", "1", "yes", "on"}
