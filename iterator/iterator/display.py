"""Print values and lists of values."""

from typing import List
import math


def convert_bool_to_answer(argument: bool):
    """Return a string-based and human-readable representation of a bool."""
    # Return a string-based and human-readable version of a bool
    if argument is True:
        return "Yes"
    else:
        return "No"
    # For instance, if argument is False then return "No"
    # For instance, if argument is True then return "Yes"



def display_list(values: List, indent=""):
    """Display the provided list when iterating and printing every indented value."""
    # iterate through all of the values inside of the list,
    # displaying them in the following fashion as an example:
    for index in range(len(values)):
        print(f"{indent}2**{int(math.log(values[index], 2))} = {values[index]}")
    # print(f"{indent}2**{index} = {values}")
    # 2**0 = 4
    # 2**1 = 8
    # 2**2 = 16
    # 2**3 = 32
    # 2**4 = 64
    # 2**5 = 128
    # 2**6 = 256
    # 2**7 = 512
    # ensure that the output is indented by the numbers of spaces in the ident
    # the display should be of the format: {indent}2**{index} = {value}
