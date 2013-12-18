#!/usr/bin/env python3.3
# vim: set fileencoding=utf-8

# Pathfinder Item Generator
#
# Copyright 2012-2013, Steven Clark.
#
# This program is free software, and is provided "as is", without warranty of
# any kind, express or implied, to the extent permitted by applicable law.
# See the full license in the file 'LICENSE'.
#
# This software includes Open Game Content.  See the file 'OGL' for more
# information.
#
'''
This module implements the various calculation stages of treasure hoard
generation.
'''

#
# Library imports

import locale
import math
import os
import random
import re
import sys

#
# Local imports

from item import Price
import rollers

#
# Module initialization

if os.name == 'posix':
    # An extremely recognizable locale string.
    locale.setlocale(locale.LC_ALL, 'en_US')
elif os.name == 'nt':
    # Windows doesn't use the sensible value.
    locale.setlocale(locale.LC_ALL, 'enu')
else:
    # My best guess for other OSes.
    try: locale.setlocale(locale.LC_ALL, 'en_US')
    except: pass


#
# Constants

# Lowest APL, inclusive, involved in UE formulas.
APL_LOW = 1

# Highest APL, inclusive, involved in UI formulas.
APL_HIGH = 20

# Rate of XP/treasure progression
RATES = ['slow', 'medium', 'fast']

# Some monsters have more treasure than others. "None" is not in this list
# because the generator wouldn't be used if there was no treasure, and "NPC
# gear" isn't a simple multiplier, so it needs special treatment.
MAGNITUDES = {
        'incidental': 0.5,
        'standard': 1.0,
        'double': 2.0,
        'triple': 3.0,
        }


#
# Variables


#
# Functions

def calculate_budget_custom(gp_in):
    # A simple reflection
    price = Price(gp_in)
    return {'budget': str(price), 'as_int': int(price.as_float())}

def calculate_budget_encounter(apl, rate, magnitude):
    try:
        apl = int(apl)
        if not(apl >= APL_LOW and apl <= APL_HIGH):
            raise AttributeError()
        if rate not in RATES:
            raise AttributeError()
        if magnitude not in MAGNITUDES:
            raise AttributeError()
    except:
        # Return an empty dict
        return {}

    return {'budget': '0 gp', 'as_int': 0}

def calculate_budget_npc_gear(npc_level, is_heroic):
    level = 0
    try:
        level = int(npc_level)
        if is_heroic: level += 1
    except:
        # Return an empty dict
        return {}

    return {'budget': 'for npc', 'as_int': 0}

def lookup_treasure_type(type_code, result):
    result['type_' + type_code] = 'going to add this'

def get_treasure_list(types):
    result = {}
    for t in types:
        lookup_treasure_type(t, result)
    return result

#
# Main Function

if __name__ == '__main__':
    pass

