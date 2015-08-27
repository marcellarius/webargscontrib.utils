__author__ = 'sam'

import webargs
from .string import lowercase, strip


def not_null(value):
    """A validation function that checks that a value isn't None."""
    return True if value is not None else False


def not_empty(value):
    """
    Check if a value is not empty.

    This is a simple check that blocks null or empty strings. It will also
    attempt to strip a string value to exclude strings containing only
    whitespace.
    :param value: A string value to check.
    :return: True if the string is not empty or only contains whitespace.
    """
    # We want to reject empty strings, or strings just containing whitespace. To do
    # this we check the result of the strip() method, if the value has one.
    if not value or not strip(value):
        return False
    else:
        return True


def choices(valid_choices, case_sensitive=False):
    """
    Create a validation function that will ensure a value is in a list of choices.

    A usage example:
      ``Arg(validate=choices(["foo", "bar"]))

    :param valid_choices: A list of valid values for this parameter
    :param case_sensitive: If false, any string-like values will be lowercased
            before comparison.  Default is `False`
    :return: A validation function
    """
    if not case_sensitive:
        valid_choices = [lowercase(c) for c in valid_choices]

    def validate_choices(value):
        if not case_sensitive:
            value = lowercase(value)
        if value in valid_choices:
            return True
        else:
            raise webargs.ValidationError(
                "Invalid value %s. Valid choices are %s" %
                (repr(value), repr(valid_choices)))

    return validate_choices


def within(min=None, max=None):
    """
    Create a validation function to check whether an argument value is within
    a specified range (inclusive).

    `min` and `max` cannot both be None.
    :param min: A lower bound for the value. Optional.
    :param max: An upper bound for the value. Optional.
    :return: A validation function
    """
    if min is None and max is None:
        raise ValueError("A min or max value must be specified")

    def validate_within(value):
        return (min is None or value >= min) and (max is None or value <= max)

    return validate_within