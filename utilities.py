#!/usr/bin/env python2
"""
    Additional utility functions.
"""

def sec_to_hms_format(sec):
    """ Convert seconds to HH:MM:SS format.

        sec: a float representing a time

        returns a string with the specified format
    """
    hh = sec // 3600
    sec %= 3600
 
    mm = sec // 60
    sec %= 60

    return '{:02d}:{:02d}:{:02d}'.format(int(hh), int(mm), int(sec))
