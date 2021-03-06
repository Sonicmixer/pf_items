#!/usr/bin/env python2
# vim: set fileencoding=utf-8

# Pathfinder Item Generator
#
# Copyright 2012-2014, Steven Clark.
#
# This program is free software, and is provided "as is", without warranty of
# any kind, express or implied, to the extent permitted by applicable law.
# See the full license in the file 'LICENSE'.
#
# This software includes Open Game Content.  See the file 'OGL' for more
# information.
#
'''
This module tests webgen.py by simulating JSON input, though with direct
function calls, not using standard input as CGI does.
'''

from __future__ import print_function

import os

import json
import webgen

# A whoooollll lotta input strings
DATA = [
        '{"mode": "echo_test"}',

        '{"mode": "settlement", "size": "thorp"}',
        '{"mode": "settlement", "size": "hamlet"}',
        '{"mode": "settlement", "size": "village"}',
        '{"mode": "settlement", "size": "small-town"}',
        '{"mode": "settlement", "size": "small town"}',
        '{"mode": "settlement", "size": "smalltown"}',
        '{"mode": "settlement", "size": "large-town"}',
        '{"mode": "settlement", "size": "large town"}',
        '{"mode": "settlement", "size": "largetown"}',
        '{"mode": "settlement", "size": "small-city"}',
        '{"mode": "settlement", "size": "small city"}',
        '{"mode": "settlement", "size": "smallcity"}',
        '{"mode": "settlement", "size": "large-city"}',
        '{"mode": "settlement", "size": "large city"}',
        '{"mode": "settlement", "size": "largecity"}',
        '{"mode": "settlement", "size": "metropolis"}',

        '{"mode": "custom", "base_value": 1000  , "q_ls_min": "1", "q_gt_min": "1", "q_ls_med": "1", "q_gt_med": "1", "q_ls_maj": "1", "q_gt_maj": "1"}',
        '{"mode": "custom", "base_value": 15000 , "q_ls_min": "1", "q_gt_min": "1", "q_ls_med": "1", "q_gt_med": "1", "q_ls_maj": "1", "q_gt_maj": "1"}',
        '{"mode": "custom", "base_value": 20000 , "q_ls_min": "1", "q_gt_min": "1", "q_ls_med": "1", "q_gt_med": "1", "q_ls_maj": "1", "q_gt_maj": "1"}',
        '{"mode": "custom", "base_value": 50000 , "q_ls_min": "1", "q_gt_min": "1", "q_ls_med": "1", "q_gt_med": "1", "q_ls_maj": "1", "q_gt_maj": "1"}',
        '{"mode": "custom", "base_value": 75000 , "q_ls_min": "1", "q_gt_min": "1", "q_ls_med": "1", "q_gt_med": "1", "q_ls_maj": "1", "q_gt_maj": "1"}',
        '{"mode": "custom", "base_value": 100000, "q_ls_min": "1", "q_gt_min": "1", "q_ls_med": "1", "q_gt_med": "1", "q_ls_maj": "1", "q_gt_maj": "1"}',
        '{"mode": "custom", "base_value": 200000, "q_ls_min": "1", "q_gt_min": "1", "q_ls_med": "1", "q_gt_med": "1", "q_ls_maj": "1", "q_gt_maj": "1"}',
        '{"mode": "custom", "base_value": 500000, "q_ls_min": "1", "q_gt_min": "1", "q_ls_med": "1", "q_gt_med": "1", "q_ls_maj": "1", "q_gt_maj": "1"}',

        '{"mode": "individual", "strength": "least minor", "type": "armor/shield"}',
        '{"mode": "individual", "strength": "least minor", "type": "weapon"}',
        '{"mode": "individual", "strength": "least minor", "type": "potion"}',
        '{"mode": "individual", "strength": "least minor", "type": "ring"}',
        '{"mode": "individual", "strength": "least minor", "type": "rod"}',
        '{"mode": "individual", "strength": "least minor", "type": "scroll"}',
        '{"mode": "individual", "strength": "least minor", "type": "staff"}',
        '{"mode": "individual", "strength": "least minor", "type": "wand"}',
        '{"mode": "individual", "strength": "least minor", "type": "wondrous"}',
        '{"mode": "individual", "strength": "least minor", "type": "belt"}',
        '{"mode": "individual", "strength": "least minor", "type": "belts"}',
        '{"mode": "individual", "strength": "least minor", "type": "body"}',
        '{"mode": "individual", "strength": "least minor", "type": "chest"}',
        '{"mode": "individual", "strength": "least minor", "type": "eyes"}',
        '{"mode": "individual", "strength": "least minor", "type": "feet"}',
        '{"mode": "individual", "strength": "least minor", "type": "hand"}',
        '{"mode": "individual", "strength": "least minor", "type": "hands"}',
        '{"mode": "individual", "strength": "least minor", "type": "head"}',
        '{"mode": "individual", "strength": "least minor", "type": "headband"}',
        '{"mode": "individual", "strength": "least minor", "type": "neck"}',
        '{"mode": "individual", "strength": "least minor", "type": "shoulders"}',
        '{"mode": "individual", "strength": "least minor", "type": "slotless"}',
        '{"mode": "individual", "strength": "least minor", "type": "wrist"}',
        '{"mode": "individual", "strength": "least minor", "type": "wrists"}',

        '{"mode": "individual", "strength": "lesser minor", "type": "armor/shield"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "weapon"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "potion"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "ring"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "rod"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "scroll"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "staff"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "wand"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "wondrous"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "belt"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "belts"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "body"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "chest"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "eyes"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "feet"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "hand"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "hands"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "head"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "headband"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "neck"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "shoulders"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "slotless"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "wrist"}',
        '{"mode": "individual", "strength": "lesser minor", "type": "wrists"}',

        '{"mode": "individual", "strength": "greater minor", "type": "armor/shield"}',
        '{"mode": "individual", "strength": "greater minor", "type": "weapon"}',
        '{"mode": "individual", "strength": "greater minor", "type": "potion"}',
        '{"mode": "individual", "strength": "greater minor", "type": "ring"}',
        '{"mode": "individual", "strength": "greater minor", "type": "rod"}',
        '{"mode": "individual", "strength": "greater minor", "type": "scroll"}',
        '{"mode": "individual", "strength": "greater minor", "type": "staff"}',
        '{"mode": "individual", "strength": "greater minor", "type": "wand"}',
        '{"mode": "individual", "strength": "greater minor", "type": "wondrous"}',
        '{"mode": "individual", "strength": "greater minor", "type": "belt"}',
        '{"mode": "individual", "strength": "greater minor", "type": "belts"}',
        '{"mode": "individual", "strength": "greater minor", "type": "body"}',
        '{"mode": "individual", "strength": "greater minor", "type": "chest"}',
        '{"mode": "individual", "strength": "greater minor", "type": "eyes"}',
        '{"mode": "individual", "strength": "greater minor", "type": "feet"}',
        '{"mode": "individual", "strength": "greater minor", "type": "hand"}',
        '{"mode": "individual", "strength": "greater minor", "type": "hands"}',
        '{"mode": "individual", "strength": "greater minor", "type": "head"}',
        '{"mode": "individual", "strength": "greater minor", "type": "headband"}',
        '{"mode": "individual", "strength": "greater minor", "type": "neck"}',
        '{"mode": "individual", "strength": "greater minor", "type": "shoulders"}',
        '{"mode": "individual", "strength": "greater minor", "type": "slotless"}',
        '{"mode": "individual", "strength": "greater minor", "type": "wrist"}',
        '{"mode": "individual", "strength": "greater minor", "type": "wrists"}',

        '{"mode": "individual", "strength": "lesser medium", "type": "armor/shield"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "weapon"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "potion"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "ring"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "rod"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "scroll"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "staff"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "wand"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "wondrous"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "belt"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "belts"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "body"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "chest"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "eyes"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "feet"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "hand"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "hands"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "head"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "headband"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "neck"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "shoulders"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "slotless"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "wrist"}',
        '{"mode": "individual", "strength": "lesser medium", "type": "wrists"}',

        '{"mode": "individual", "strength": "greater medium", "type": "armor/shield"}',
        '{"mode": "individual", "strength": "greater medium", "type": "weapon"}',
        '{"mode": "individual", "strength": "greater medium", "type": "potion"}',
        '{"mode": "individual", "strength": "greater medium", "type": "ring"}',
        '{"mode": "individual", "strength": "greater medium", "type": "rod"}',
        '{"mode": "individual", "strength": "greater medium", "type": "scroll"}',
        '{"mode": "individual", "strength": "greater medium", "type": "staff"}',
        '{"mode": "individual", "strength": "greater medium", "type": "wand"}',
        '{"mode": "individual", "strength": "greater medium", "type": "wondrous"}',
        '{"mode": "individual", "strength": "greater medium", "type": "belt"}',
        '{"mode": "individual", "strength": "greater medium", "type": "belts"}',
        '{"mode": "individual", "strength": "greater medium", "type": "body"}',
        '{"mode": "individual", "strength": "greater medium", "type": "chest"}',
        '{"mode": "individual", "strength": "greater medium", "type": "eyes"}',
        '{"mode": "individual", "strength": "greater medium", "type": "feet"}',
        '{"mode": "individual", "strength": "greater medium", "type": "hand"}',
        '{"mode": "individual", "strength": "greater medium", "type": "hands"}',
        '{"mode": "individual", "strength": "greater medium", "type": "head"}',
        '{"mode": "individual", "strength": "greater medium", "type": "headband"}',
        '{"mode": "individual", "strength": "greater medium", "type": "neck"}',
        '{"mode": "individual", "strength": "greater medium", "type": "shoulders"}',
        '{"mode": "individual", "strength": "greater medium", "type": "slotless"}',
        '{"mode": "individual", "strength": "greater medium", "type": "wrist"}',
        '{"mode": "individual", "strength": "greater medium", "type": "wrists"}',

        '{"mode": "individual", "strength": "lesser major", "type": "armor/shield"}',
        '{"mode": "individual", "strength": "lesser major", "type": "weapon"}',
        '{"mode": "individual", "strength": "lesser major", "type": "potion"}',
        '{"mode": "individual", "strength": "lesser major", "type": "ring"}',
        '{"mode": "individual", "strength": "lesser major", "type": "rod"}',
        '{"mode": "individual", "strength": "lesser major", "type": "scroll"}',
        '{"mode": "individual", "strength": "lesser major", "type": "staff"}',
        '{"mode": "individual", "strength": "lesser major", "type": "wand"}',
        '{"mode": "individual", "strength": "lesser major", "type": "wondrous"}',
        '{"mode": "individual", "strength": "lesser major", "type": "belt"}',
        '{"mode": "individual", "strength": "lesser major", "type": "belts"}',
        '{"mode": "individual", "strength": "lesser major", "type": "body"}',
        '{"mode": "individual", "strength": "lesser major", "type": "chest"}',
        '{"mode": "individual", "strength": "lesser major", "type": "eyes"}',
        '{"mode": "individual", "strength": "lesser major", "type": "feet"}',
        '{"mode": "individual", "strength": "lesser major", "type": "hand"}',
        '{"mode": "individual", "strength": "lesser major", "type": "hands"}',
        '{"mode": "individual", "strength": "lesser major", "type": "head"}',
        '{"mode": "individual", "strength": "lesser major", "type": "headband"}',
        '{"mode": "individual", "strength": "lesser major", "type": "neck"}',
        '{"mode": "individual", "strength": "lesser major", "type": "shoulders"}',
        '{"mode": "individual", "strength": "lesser major", "type": "slotless"}',
        '{"mode": "individual", "strength": "lesser major", "type": "wrist"}',
        '{"mode": "individual", "strength": "lesser major", "type": "wrists"}',

        '{"mode": "individual", "strength": "greater major", "type": "armor/shield"}',
        '{"mode": "individual", "strength": "greater major", "type": "ring"}',
        '{"mode": "individual", "strength": "greater major", "type": "rod"}',
        '{"mode": "individual", "strength": "greater major", "type": "scroll"}',
        '{"mode": "individual", "strength": "greater major", "type": "staff"}',
        '{"mode": "individual", "strength": "greater major", "type": "wand"}',
        '{"mode": "individual", "strength": "greater major", "type": "wondrous"}',
        '{"mode": "individual", "strength": "greater major", "type": "belt"}',
        '{"mode": "individual", "strength": "greater major", "type": "belts"}',
        '{"mode": "individual", "strength": "greater major", "type": "body"}',
        '{"mode": "individual", "strength": "greater major", "type": "chest"}',
        '{"mode": "individual", "strength": "greater major", "type": "eyes"}',
        '{"mode": "individual", "strength": "greater major", "type": "feet"}',
        '{"mode": "individual", "strength": "greater major", "type": "hand"}',
        '{"mode": "individual", "strength": "greater major", "type": "hands"}',
        '{"mode": "individual", "strength": "greater major", "type": "head"}',
        '{"mode": "individual", "strength": "greater major", "type": "headband"}',
        '{"mode": "individual", "strength": "greater major", "type": "neck"}',
        '{"mode": "individual", "strength": "greater major", "type": "shoulders"}',
        '{"mode": "individual", "strength": "greater major", "type": "slotless"}',
        '{"mode": "individual", "strength": "greater major", "type": "wrist"}',
        '{"mode": "individual", "strength": "greater major", "type": "wrists"}',
        '{"mode": "faiiiil"}',
        '{"mode": "hoard_budget", "type": "custom", "custom_gp":"3000"}',
        '{"mode": "hoard_budget", "type": "encounter", "apl": 1, "rate": "slow", "magnitude": "standard"}',
        '{"mode": "hoard_budget", "type": "encounter", "apl": 1, "rate": "medium", "magnitude": "standard"}',
        '{"mode": "hoard_budget", "type": "encounter", "apl": 1, "rate": "fast", "magnitude": "standard"}',
        '{"mode": "hoard_budget", "type": "encounter", "apl": 1, "rate": "medium", "magnitude": "incidental"}',
        '{"mode": "hoard_budget", "type": "encounter", "apl": 1, "rate": "medium", "magnitude": "double"}',
        '{"mode": "hoard_budget", "type": "encounter", "apl": 1, "rate": "medium", "magnitude": "triple"}',
        '{"mode": "hoard_budget", "type": "npc_gear", "npc_level": 1, "heroic": "false"}',
        '{"mode": "hoard_types", "type_a": "true"}',
        '{"mode": "hoard_types", "type_a": "true", "type_b": "true", "type_c": "true", "type_d": "true", "type_e": "true", "type_f": "true", "type_g": "true", "type_h": "true", "type_i": "true"}',
        ]

OVERRIDE_DATA = [
        #"{'b': [{'cost': 10, 'index': 0, 'count': 0, 'item': '10 gp', 'description': 'Grade 1 gemstone'}, {'cost': 15, 'index': 1, 'count': 0, 'item': '15 gp', 'description': '2d6 × 10 cp, 4d8 sp, 1d4 gp, grade 1 gemstone'}, {'cost': 25, 'index': 2, 'count': 0, 'item': '25 gp', 'description': '5d10 sp, 1d4 gp, two grade 1 gemstones'}, {'cost': 50, 'index': 3, 'count': 0, 'item': '50 gp', 'description': 'Grade 2 gemstone'}, {'cost': 50, 'index': 4, 'count': 0, 'item': '50 gp', 'description': '3d6 × 10 sp, 3d6 gp, three grade 1 gemstones'}, {'cost': 75, 'index': 5, 'count': 0, 'item': '75 gp', 'description': '1d4 × 10 sp, 1d4 gp, two grade 1 gemstones, grade 2 gemstone'}, {'cost': 100, 'index': 6, 'count': 0, 'item': '100 gp', 'description': 'Grade 3 gemstone'}, {'cost': 100, 'index': 7, 'count': 0, 'item': '100 gp', 'description': '3d8 × 10 sp, 4d8 gp, two grade 1 gemstones, grade 2 gemstone'}, {'cost': 150, 'index': 8, 'count': 0, 'item': '150 gp', 'description': 'Grade 2 gemstone, grade 3 gemstone'}, {'cost': 200, 'index': 9, 'count': 0, 'item': '200 gp', 'description': '3d6 × 10 sp, 2d4x10 gp, four grade 1 gemstones, grade 3 gemstone'}, {'cost': 250, 'index': 10, 'count': 0, 'item': '250 gp', 'description': '2d4 × 10 gp, two grade 2 gemstones, grade 3 gemstone'}, {'cost': 500, 'index': 11, 'count': 0, 'item': '500 gp', 'description': 'Grade 4 gemstone'}, {'cost': 500, 'index': 12, 'count': 0, 'item': '500 gp', 'description': '2d4 × 10 gp, 2d4 pp, two grade 2 gemstones, three grade 3 gemstones'}, {'cost': 750, 'index': 13, 'count': 0, 'item': '750 gp', 'description': '2d4 × 10 gp, two grade 2 gemstones, grade 3 gemstone, grade 4 gemstone'}, {'cost': 1000, 'index': 14, 'count': 0, 'item': '1,000 gp', 'description': 'Grade 5 gemstone'}, {'cost': 1000, 'index': 15, 'count': 0, 'item': '1,000 gp', 'description': '3d6 × 10 gp, 4d4 pp, three grade 3 gemstones, grade 4 gemstone'}, {'cost': 2500, 'index': 16, 'count': 0, 'item': '2,500 gp', 'description': '2d4 × 100 gp, two grade 4 gemstones, grade 5 gemstone'}, {'cost': 5000, 'index': 17, 'count': 0, 'item': '5,000 gp', 'description': 'Grade 6 gemstone'}, {'cost': 5000, 'index': 18, 'count': 0, 'item': '5,000 gp', 'description': '2d4 × 100 gp, 2d4x10 pp, two grade 4 gemstones, three grade 5 gemstones'}, {'cost': 10000, 'index': 19, 'count': 0, 'item': '10,000 gp', 'description': 'Five grade 5 gemstones, grade 6 gemstone'}, {'cost': 20000, 'index': 20, 'count': 0, 'item': '20,000 gp', 'description': '4d8 × 100 gp, 6d10x10 pp, three grade 6 gemstones'}, {'cost': 50000, 'index': 21, 'count': 0, 'item': '50,000 gp', 'description': '4d4 × 10 pp, ten grade 3 gemstones, four grade 4 gemstones, six grade 5 gemstones, eight grade 6 gemstones'}], 'c': [{'cost': 50, 'index': 0, 'count': 0, 'item': '50 gp', 'description': 'Grade 1 art object'}, {'cost': 100, 'index': 1, 'count': 0, 'item': '100 gp', 'description': 'Grade 2 art object'}, {'cost': 100, 'index': 2, 'count': 0, 'item': '100 gp', 'description': 'Two grade 1 art objects'}, {'cost': 150, 'index': 3, 'count': 0, 'item': '150 gp', 'description': 'Grade 1 art object, grade 2 art object'}, {'cost': 200, 'index': 4, 'count': 0, 'item': '200 gp', 'description': 'Two grade 2 art objects'}, {'cost': 250, 'index': 5, 'count': 0, 'item': '250 gp', 'description': 'Three grade 1 art objects, grade 2 art object'}, {'cost': 500, 'index': 6, 'count': 0, 'item': '500 gp', 'description': 'Grade 3 art object'}, {'cost': 500, 'index': 7, 'count': 0, 'item': '500 gp', 'description': 'Four grade 1 art objects, three grade 2 art objects'}, {'cost': 750, 'index': 8, 'count': 0, 'item': '750 gp', 'description': 'Three grade 1 art objects, two grade 2 art objects, grade 3 art object'}, {'cost': 1000, 'index': 9, 'count': 0, 'item': '1,000 gp', 'description': 'Grade 4 art object'}, {'cost': 1000, 'index': 10, 'count': 0, 'item': '1,000 gp', 'description': 'Two grade 3 art objects'}, {'cost': 1500, 'index': 11, 'count': 0, 'item': '1,500 gp', 'description': 'Grade 3 art object, grade 4 art object'}, {'cost': 2000, 'index': 12, 'count': 0, 'item': '2,000 gp', 'description': 'Two grade 4 art objects'}, {'cost': 2500, 'index': 13, 'count': 0, 'item': '2,500 gp', 'description': 'Five grade 2 art objects, two grade 3 art objects, grade 4 art object'}, {'cost': 5000, 'index': 14, 'count': 0, 'item': '5,000 gp', 'description': 'Grade 5 art object'}, {'cost': 5000, 'index': 15, 'count': 0, 'item': '5,000 gp', 'description': 'Four grade 3 art objects, three grade 4 art objects'}, {'cost': 7500, 'index': 16, 'count': 0, 'item': '7,500 gp', 'description': 'Grade 3 art object, two grade 4 art objects, grade 5 art object'}, {'cost': 10000, 'index': 17, 'count': 0, 'item': '10,000 gp', 'description': 'Grade 6 art object'}, {'cost': 10000, 'index': 18, 'count': 0, 'item': '10,000 gp', 'description': 'Five grade 4 art objects, grade 5 art object'}, {'cost': 15000, 'index': 19, 'count': 0, 'item': '15,000 gp', 'description': 'Grade 5 art object, grade 6 art object'}, {'cost': 20000, 'index': 20, 'count': 0, 'item': '20,000 gp', 'description': 'Two grade 5 art objects, grade 6 art object'}, {'cost': 50000, 'index': 21, 'count': 0, 'item': '50,000 gp', 'description': 'Ten grade 3 art objects, five grade 4 art objects, four grade 5 art objects, two grade 6 art objects'}], 'a': [{'cost': 1, 'index': 0, 'count': 0, 'item': '1 gp', 'description': '5d10 cp, 3d4 sp'}, {'cost': 5, 'index': 1, 'count': 0, 'item': '5 gp', 'description': '2d6 × 10 cp, 4d8 sp, 1d4 gp'}, {'cost': 10, 'index': 2, 'count': 0, 'item': '10 gp', 'description': '5d10 × 10 cp, 5d10 sp, 1d8 gp'}, {'cost': 25, 'index': 3, 'count': 0, 'item': '25 gp', 'description': '2d4 × 100 cp, 3d6 × 10 sp, 4d4 gp'}, {'cost': 50, 'index': 4, 'count': 0, 'item': '50 gp', 'description': '4d4 × 100 cp, 4d6 × 10 sp, 8d6 gp'}, {'cost': 100, 'index': 5, 'count': 0, 'item': '100 gp', 'description': '6d8 × 10 sp, 3d4 × 10 gp'}, {'cost': 200, 'index': 6, 'count': 0, 'item': '200 gp', 'description': '2d4 × 100 sp, 4d4 × 10 gp, 2d4 pp'}, {'cost': 500, 'index': 7, 'count': 0, 'item': '500 gp', 'description': '6d6 × 10 gp, 8d6 pp'}, {'cost': 1000, 'index': 8, 'count': 0, 'item': '1,000 gp', 'description': '2d4 × 100 gp, 10d10 pp'}, {'cost': 5000, 'index': 9, 'count': 0, 'item': '5,000 gp', 'description': '4d8 × 100 gp, 6d10 × 10 pp'}, {'cost': 10000, 'index': 10, 'count': 0, 'item': '10,000 gp', 'description': '2d4 × 1,000 gp, 12d8 × 10 pp'}, {'cost': 50000, 'index': 11, 'count': 1, 'item': '50,000 gp', 'description': '2d6 × 1,000 gp, 8d10 × 100 pp'}], 'f': [{'cost': 50, 'index': 0, 'count': 0, 'item': '50 gp', 'description': '2d4 × 10 sp, 2d4 gp, lesser minor potion'}, {'cost': 250, 'index': 1, 'count': 0, 'item': '250 gp', 'description': '2d4 × 10 sp, 2d4 gp, masterwork light armor or shield, lesser minor potion'}, {'cost': 350, 'index': 2, 'count': 0, 'item': '350 gp', 'description': '2d4 × 10 sp, 2d4 gp, masterwork medium armor, lesser minor potion'}, {'cost': 400, 'index': 3, 'count': 0, 'item': '400 gp', 'description': '2d4 × 10 sp, 2d4 gp, masterwork weapon, lesser minor potion'}, {'cost': 500, 'index': 4, 'count': 0, 'item': '500 gp', 'description': 'Masterwork weapon, greater minor potion'}, {'cost': 750, 'index': 5, 'count': 0, 'item': '750 gp', 'description': '6d6 gp, masterwork medium armor, masterwork weapon, two lesser minor potions'}, {'cost': 1000, 'index': 6, 'count': 0, 'item': '1,000 gp', 'description': 'Masterwork heavy armor'}, {'cost': 1500, 'index': 7, 'count': 0, 'item': '1,500 gp', 'description': 'Masterwork heavy armor, masterwork weapon, greater minor potion'}, {'cost': 2000, 'index': 8, 'count': 0, 'item': '2,000 gp', 'description': 'Lesser minor armor, masterwork weapon, two greater minor potions'}, {'cost': 3, 'index': 9, 'count': 0, 'item': '3.000 gp', 'description': 'Masterwork medium armor, lesser minor weapon, greater minor potion'}, {'cost': 4000, 'index': 10, 'count': 0, 'item': '4,000 gp', 'description': 'Lesser minor armor, masterwork weapon, lesser minor wondrous item, greater minor potion'}, {'cost': 5000, 'index': 11, 'count': 0, 'item': '5,000 gp', 'description': 'Masterwork medium armor, lesser minor weapon, lesser minor wondrous item, greater minor potion'}, {'cost': 6000, 'index': 12, 'count': 0, 'item': '6,000 gp', 'description': 'Lesser minor armor, lesser minor weapon, lesser minor wondrous item'}, {'cost': 7500, 'index': 13, 'count': 0, 'item': '7,500 gp', 'description': 'Greater minor armor, lesser minor weapon, lesser minor ring'}, {'cost': 10000, 'index': 14, 'count': 0, 'item': '10,000 gp', 'description': 'Greater minor armor, lesser minor weapon, lesser minor ring, lesser minor wondrous item, three greater minor potions'}, {'cost': 10000, 'index': 15, 'count': 0, 'item': '10,000 gp', 'description': 'Greater minor armor, greater minor weapon, two greater medium potions'}, {'cost': 12500, 'index': 16, 'count': 0, 'item': '12,500 gp', 'description': 'Greater minor armor, lesser minor weapon, greater minor wondrous item, two greater medium potions'}, {'cost': 15000, 'index': 17, 'count': 0, 'item': '15,000 gp', 'description': 'Greater minor armor, greater minor weapon, greater minor ring'}, {'cost': 20000, 'index': 18, 'count': 0, 'item': '20,000 gp', 'description': 'Lesser medium armor, greater minor weapon, greater minor wondrous item, two greater medium potions'}, {'cost': 25000, 'index': 19, 'count': 0, 'item': '25,000 gp', 'description': 'Lesser medium armor, lesser medium weapon, lesser minor ring, lesser minor wondrous item, two greater medium potions'}, {'cost': 30000, 'index': 20, 'count': 0, 'item': '30,000 gp', 'description': 'Lesser medium armor, lesser medium weapon, two lesser minor rings, greater minor wondrous items'}, {'cost': 40000, 'index': 21, 'count': 0, 'item': '40,000 gp', 'description': 'Lesser medium armor, lesser medium weapon, lesser medium ring, greater minor wondrous item, two greater medium potions'}, {'cost': 50000, 'index': 22, 'count': 0, 'item': '50,000 gp', 'description': 'Greater medium armor, greater medium weapon, lesser medium wondrous item, two lesser major potions'}, {'cost': 60000, 'index': 23, 'count': 0, 'item': '60,000 gp', 'description': 'Greater medium armor, greater medium weapon, two greater minor rings, two greater minor wondrous items'}, {'cost': 75000, 'index': 24, 'count': 0, 'item': '75,000 gp', 'description': 'Lesser major armor, greater medium weapon, greater minor ring, greater medium wondrous item, three greater major potions'}, {'cost': 100000, 'index': 25, 'count': 0, 'item': '100,000 gp', 'description': 'Lesser major armor, lesser major weapon, lesser medium ring, greater minor ring, two lesser medium wondrous items'}], 'g': [{'cost': 50, 'index': 0, 'count': 0, 'item': '50 gp', 'description': '2d4 × 10 sp, 2d4 gp, lesser minor potion'}, {'cost': 75, 'index': 1, 'count': 0, 'item': '75 gp', 'description': '2d4 gp, lesser minor potion, lesser minor scroll'}, {'cost': 100, 'index': 2, 'count': 0, 'item': '100 gp', 'description': 'Lesser minor potion, two lesser minor scrolls'}, {'cost': 150, 'index': 3, 'count': 0, 'item': '150 gp', 'description': 'Lesser minor scroll, greater minor scroll'}, {'cost': 200, 'index': 4, 'count': 0, 'item': '200 gp', 'description': 'Two lesser minor potions, greater minor scroll'}, {'cost': 250, 'index': 5, 'count': 0, 'item': '250 gp', 'description': 'Two greater minor scrolls'}, {'cost': 500, 'index': 6, 'count': 0, 'item': '500 gp', 'description': 'Three lesser minor potions, three greater minor scrolls'}, {'cost': 750, 'index': 7, 'count': 0, 'item': '750 gp', 'description': 'Greater minor potion, lesser minor wand'}, {'cost': 1000, 'index': 8, 'count': 0, 'item': '1,000 gp', 'description': '7d6 gp, three greater minor scrolls, lesser minor wand'}, {'cost': 1500, 'index': 9, 'count': 0, 'item': '1,500 gp', 'description': '3d6 × 10 gp, Lesser medium potion, lesser medium scroll, lesser minor wand'}, {'cost': 2000, 'index': 10, 'count': 0, 'item': '2,000 gp', 'description': '2d4 × 10 gp, masterwork weapon, two lesser medium scrolls, lesser minor wand'}, {'cost': 2500, 'index': 11, 'count': 0, 'item': '2,500 gp', 'description': 'Two greater medium potions, greater minor wand'}, {'cost': 3000, 'index': 12, 'count': 0, 'item': '3,000 gp', 'description': 'Greater medium potion, two lesser medium scrolls, greater minor wand'}, {'cost': 4000, 'index': 13, 'count': 0, 'item': '4,000 gp', 'description': 'Lesser minor wondrous item, greater medium potion, greater minor wand'}, {'cost': 5000, 'index': 14, 'count': 0, 'item': '5,000 gp', 'description': 'Lesser minor ring, lesser minor wondrous item, two lesser medium scrolls'}, {'cost': 6000, 'index': 15, 'count': 0, 'item': '6,000 gp', 'description': 'Lesser minor ring, lesser minor wondrous item, greater medium potion, greater minor wand'}, {'cost': 7500, 'index': 16, 'count': 0, 'item': '7,500 gp', 'description': 'Two greater medium potions, lesser minor scroll, lesser medium wand'}, {'cost': 10000, 'index': 17, 'count': 0, 'item': '10,000 gp', 'description': 'Lesser minor ring, lesser minor wondrous item, lesser medium wand'}, {'cost': 12500, 'index': 18, 'count': 0, 'item': '12,500 gp', 'description': 'Lesser minor ring, greater minor wondrous item, two greater medium scrolls, two greater minor wands'}, {'cost': 15000, 'index': 19, 'count': 0, 'item': '15,000 gp', 'description': 'Lesser minor ring, lesser medium rod, lesser medium wand'}, {'cost': 20000, 'index': 20, 'count': 0, 'item': '20,000 gp', 'description': 'Greater minor ring, greater minor wondrous item, greater medium potion, two greater medium scrolls, lesser medium wand'}, {'cost': 25000, 'index': 21, 'count': 0, 'item': '25,000 gp', 'description': 'Lesser minor ring, lesser medium wand, greater medium wand, greater minor wondrous item'}, {'cost': 30000, 'index': 22, 'count': 0, 'item': '30,000 gp', 'description': 'Greater minor ring, lesser medium wondrous item, lesser major scroll, greater medium wand'}, {'cost': 40000, 'index': 23, 'count': 0, 'item': '40,000 gp', 'description': 'Lesser minor weapon, lesser medium staff, greater medium rod, two lesser minor wondrous items, lesser medium wand'}, {'cost': 50000, 'index': 24, 'count': 0, 'item': '50,000 gp', 'description': 'Greater minor ring, two lesser medium wondrous items, lesser major potion, three greater medium scrolls, lesser major wand'}, {'cost': 60000, 'index': 25, 'count': 0, 'item': '60,000 gp', 'description': 'Lesser medium staff, greater medium rod, greater medium wondrous item, greater medium potion, two lesser major scrolls, lesser medium wand'}, {'cost': 75000, 'index': 26, 'count': 0, 'item': '75,000 gp', 'description': 'Lesser minor weapon, greater medium staff, greater medium wondrous item, three greater major scrolls, greater major wand'}, {'cost': 100000, 'index': 27, 'count': 0, 'item': '100,000 gp', 'description': 'Lesser major ring, greater medium rod, lesser major staff, lesser major scroll, greater medium wand'}], 'd': [{'cost': 50, 'index': 0, 'count': 0, 'item': '50 gp', 'description': '3d6 × 10 sp, 4d4 gp, lesser minor scroll'}, {'cost': 50, 'index': 1, 'count': 0, 'item': '50 gp', 'description': '2d4 × 10 sp, 2d4 gp, lesser minor potion'}, {'cost': 100, 'index': 2, 'count': 0, 'item': '100 gp', 'description': '4d6 × 10 sp, 3d10 gp, lesser minor potion, lesser minor scroll'}, {'cost': 150, 'index': 3, 'count': 0, 'item': '150 gp', 'description': '2d4 × 10 sp, 6d6 gp, greater minor scroll'}, {'cost': 200, 'index': 4, 'count': 0, 'item': '200 gp', 'description': '2d4 × 10 sp, 4d6 gp, greater minor potion, lesser minor scroll'}, {'cost': 250, 'index': 5, 'count': 0, 'item': '250 gp', 'description': '3d6 × 10 sp, 3d6 gp, 1d4 pp, two lesser minor potions, greater minor scroll'}, {'cost': 300, 'index': 6, 'count': 0, 'item': '300 gp', 'description': '2d4 × 10 sp, 6d6 gp, greater minor potion, greater minor scroll'}, {'cost': 400, 'index': 7, 'count': 0, 'item': '400 gp', 'description': 'Greater minor potion, two greater minor scrolls'}, {'cost': 500, 'index': 8, 'count': 0, 'item': '500 gp', 'description': '2d4 × 10 gp, 1d4 pp, lesser medium potion, greater minor scroll'}, {'cost': 500, 'index': 9, 'count': 0, 'item': '500 gp', 'description': '2d4 × 10 gp, 1d4 pp, two greater minor potions, greater minor scroll'}, {'cost': 750, 'index': 10, 'count': 0, 'item': '750 gp', 'description': '7d6 gp, greater minor scroll, lesser minor wand'}, {'cost': 1000, 'index': 11, 'count': 0, 'item': '1,000 gp', 'description': '4d4 × 10 gp, 3d6 pp, lesser medium potion, lesser medium scroll'}, {'cost': 1000, 'index': 12, 'count': 0, 'item': '1,000 gp', 'description': '2d4 × 10 gp, 2d4 pp, lesser medium potion, lesser minor wand'}, {'cost': 1500, 'index': 13, 'count': 0, 'item': '1,500 gp', 'description': 'Greater minor wand'}, {'cost': 1500, 'index': 14, 'count': 0, 'item': '1,500 gp', 'description': '4d4 × 10 gp, 3d6 pp, greater medium potion, greater medium scroll'}, {'cost': 2000, 'index': 15, 'count': 0, 'item': '2,000 gp', 'description': 'Greater medium potion, greater minor wand'}, {'cost': 2000, 'index': 16, 'count': 0, 'item': '2,000 gp', 'description': '2d4 × 10 gp, 2d4 pp, lesser medium potion, two greater medium scrolls'}, {'cost': 3000, 'index': 17, 'count': 0, 'item': '3,000 gp', 'description': '3d6 × 10 gp, 4d4 pp, greater medium potion, greater medium scroll, greater minor wand'}, {'cost': 4000, 'index': 18, 'count': 0, 'item': '4,000 gp', 'description': '3d6 × 10 gp, 4d4 pp, greater medium scroll, two greater minor wands'}, {'cost': 5000, 'index': 19, 'count': 0, 'item': '5,000 gp', 'description': '2d4 × 10 gp, 2d4 pp, three lesser major potions, two greater medium scrolls, greater minor wand'}, {'cost': 7500, 'index': 20, 'count': 0, 'item': '7,500 gp', 'description': '2d6 pp, lesser major scroll, lesser medium wand'}, {'cost': 7500, 'index': 21, 'count': 0, 'item': '7,500 gp', 'description': '5d6 pp, two greater major potions, two greater major scrolls'}, {'cost': 10000, 'index': 22, 'count': 0, 'item': '10,000 gp', 'description': 'Greater medium wand'}, {'cost': 10000, 'index': 23, 'count': 0, 'item': '10,000 gp', 'description': '4d6 pp, greater major potion, greater major scroll, lesser medium wand'}, {'cost': 15000, 'index': 24, 'count': 0, 'item': '15,000 gp', 'description': 'Lesser major wand'}, {'cost': 15000, 'index': 25, 'count': 0, 'item': '15,000 gp', 'description': '9d10 pp, three greater major potions, two lesser major scrolls, greater medium wand'}, {'cost': 20000, 'index': 26, 'count': 0, 'item': '20,000 gp', 'description': '4d4 × 10 gp, 2d4x10 pp, two greater major potions, greater major scroll, lesser major wand'}, {'cost': 20000, 'index': 27, 'count': 0, 'item': '20,000 gp', 'description': '6d6 × 10 gp, three lesser major potions, greater major wand'}, {'cost': 25000, 'index': 28, 'count': 0, 'item': '25,000 gp', 'description': 'Five greater major scrolls, greater medium wand'}, {'cost': 30000, 'index': 29, 'count': 0, 'item': '30,000 gp', 'description': '6d6 pp, four greater major potions, three greater major scrolls, greater major wand'}, {'cost': 50000, 'index': 30, 'count': 0, 'item': '50,000 gp', 'description': '8d4 × 10 pp, four greater major scrolls, two greater major wands'}], 'e': [{'cost': 200, 'index': 0, 'count': 0, 'item': '200 gp', 'description': 'Masterwork light armor or shield'}, {'cost': 300, 'index': 1, 'count': 0, 'item': '300 gp', 'description': 'Masterwork medium armor'}, {'cost': 350, 'index': 2, 'count': 0, 'item': '350 gp', 'description': 'Masterwork weapon'}, {'cost': 1000, 'index': 3, 'count': 0, 'item': '1,000 gp', 'description': 'Masterwork heavy armor'}, {'cost': 1500, 'index': 4, 'count': 0, 'item': '1,500 gp', 'description': 'Lesser minor armor'}, {'cost': 2500, 'index': 5, 'count': 0, 'item': '2,500 gp', 'description': 'Lesser minor weapon'}, {'cost': 3000, 'index': 6, 'count': 0, 'item': '3,000 gp', 'description': 'Greater minor armor'}, {'cost': 3000, 'index': 7, 'count': 0, 'item': '3,000 gp', 'description': 'Masterwork medium armor, masterwork shield, lesser minor weapon'}, {'cost': 4000, 'index': 8, 'count': 0, 'item': '4,000 gp', 'description': 'Lesser minor armor, lesser minor weapon'}, {'cost': 5500, 'index': 9, 'count': 0, 'item': '5,500 gp', 'description': 'Greater minor armor, lesser minor weapon'}, {'cost': 6000, 'index': 10, 'count': 0, 'item': '6,000 gp', 'description': 'Greater minor weapon'}, {'cost': 7500, 'index': 11, 'count': 0, 'item': '7,500 gp', 'description': 'Lesser minor armor, greater minor weapon'}, {'cost': 8000, 'index': 12, 'count': 0, 'item': '8,000 gp', 'description': 'Greater minor armor, two lesser minor weapons'}, {'cost': 9000, 'index': 13, 'count': 0, 'item': '9,000 gp', 'description': 'Greater minor armor, greater minor weapon'}, {'cost': 10000, 'index': 14, 'count': 0, 'item': '10,000 gp', 'description': 'Lesser medium armor, lesser minor weapon'}, {'cost': 13000, 'index': 15, 'count': 0, 'item': '13,000 gp', 'description': 'Lesser medium weapon'}, {'cost': 13000, 'index': 16, 'count': 0, 'item': '13,000 gp', 'description': 'Lesser medium armor, greater minor weapon'}, {'cost': 15000, 'index': 17, 'count': 0, 'item': '15,000 gp', 'description': 'Greater medium armor, lesser minor weapon'}, {'cost': 20000, 'index': 18, 'count': 0, 'item': '20,000 gp', 'description': 'Lesser medium armor, lesser medium weapon'}, {'cost': 25000, 'index': 19, 'count': 0, 'item': '25,000 gp', 'description': 'Greater minor armor, greater medium weapon'}, {'cost': 30000, 'index': 20, 'count': 0, 'item': '30,000 gp', 'description': 'Lesser major armor, lesser minor weapon, greater minor weapon'}, {'cost': 30000, 'index': 21, 'count': 0, 'item': '30,000 gp', 'description': 'Lesser medium armor, greater medium weapon'}, {'cost': 35000, 'index': 22, 'count': 0, 'item': '35,000 gp', 'description': 'Lesser major armor, lesser medium weapon'}, {'cost': 35000, 'index': 23, 'count': 0, 'item': '35,000 gp', 'description': 'Lesser minor armor, lesser major weapon'}, {'cost': 40000, 'index': 24, 'count': 0, 'item': '40,000 gp', 'description': 'Greater major armor, greater minor weapon'}, {'cost': 50000, 'index': 25, 'count': 0, 'item': '50,000 gp', 'description': 'Greater major armor, lesser medium weapon'}, {'cost': 75000, 'index': 26, 'count': 0, 'item': '75,000 gp', 'description': 'Greater minor armor, greater major weapon'}, {'cost': 100000, 'index': 27, 'count': 0, 'item': '100,000 gp', 'description': 'Greater major armor, greater major weapon'}], 'h': [{'cost': 500, 'index': 0, 'count': 0, 'item': '500 gp', 'description': '4d4 × 100 cp, 3d6 × 10 sp, 2d4 × 10 gp, masterwork weapon, lesser minor potion, lesser minor scroll, grade 2 gemstone'}, {'cost': 1000, 'index': 1, 'count': 0, 'item': '1,000 gp', 'description': '2d4 × 100 cp, 2d6 × 100 sp, 6d6 gp, greater minor potion, greater minor scroll, lesser minor wand, three grade 1 gemstones'}, {'cost': 2500, 'index': 2, 'count': 0, 'item': '2,500 gp', 'description': '3d6 × 10 sp, 2d4 gp, masterwork heavy armor, masterwork weapon, two lesser medium potions, two greater minor scrolls, grade 2 gemstone'}, {'cost': 5000, 'index': 3, 'count': 0, 'item': '5,000 gp', 'description': '2d4 × 10 gp, 4d6 pp, masterwork weapon, lesser minor ring, greater medium potion, lesser medium scroll, greater minor wand'}, {'cost': 7500, 'index': 4, 'count': 0, 'item': '7,500 gp', 'description': '4d4 × 10 gp, 6d6 pp, lesser minor weapon, lesser minor wondrous item, two greater medium potions, greater minor wand, two grade 3 gemstones'}, {'cost': 10000, 'index': 5, 'count': 0, 'item': '10,000 gp', 'description': '4d8 × 10 gp, 6d10 pp, greater minor armor, lesser minor ring, lesser minor wondrous item, lesser medium scroll, greater minor wand, grade 4 gemstone'}, {'cost': 15000, 'index': 6, 'count': 0, 'item': '15,000 gp', 'description': '4d4 × 10 gp, 4d4 × 10 pp, greater minor armor, lesser minor wondrous item, two greater medium potions, two greater medium scrolls, lesser medium wand, one grade 3 gemstone'}, {'cost': 20000, 'index': 7, 'count': 0, 'item': '20,000 gp', 'description': '2d4 × 10 pp, greater minor ring, two lesser minor wondrous items, two greater medium potions, two lesser major scrolls, lesser medium wand'}, {'cost': 25000, 'index': 8, 'count': 0, 'item': '25,000 gp', 'description': '6d10 × 10 gp, 6d6 pp, lesser medium armor, lesser minor weapon, greater minor wondrous item, two lesser major scrolls, lesser medium wand, grade 4 gemstone'}, {'cost': 30000, 'index': 9, 'count': 0, 'item': '30,000 gp', 'description': '6d6 × 10 gp, 2d4 × 10 pp, greater minor weapon, lesser medium wondrous item, greater medium wand, three grade 3 gemstones'}, {'cost': 40000, 'index': 10, 'count': 0, 'item': '40,000 gp', 'description': '4d4 × 10 gp, 4d4 × 10 pp, lesser medium ring, lesser medium rod, two greater major potions, two lesser major scrolls, lesser major wand'}, {'cost': 50000, 'index': 11, 'count': 0, 'item': '50,000 gp', 'description': '4d4 × 10 pp, greater medium armor, lesser medium staff, lesser medium wondrous item, greater major scroll, lesser medium wand, grade 5 gemstone'}, {'cost': 75000, 'index': 12, 'count': 0, 'item': '75,000 gp', 'description': '2d8 × 100 gp, 4d4 × 10 pp, greater minor weapon, greater medium ring, greater medium staff, three greater major potions, greater major scroll, lesser major wand, grade 5 gemstone'}, {'cost': 100000, 'index': 13, 'count': 0, 'item': '100,000 gp', 'description': '8d6 × 100 gp, 4d4 × 10 pp, lesser major ring, lesser major wondrous item, three greater major potions, greater major scroll, lesser medium wand, two grade 5 gemstones, grade 6 gemstone'}], 'i': [{'cost': 5000, 'index': 0, 'count': 0, 'item': '5,000 gp', 'description': '4d4 × 1,000 cp, 6d6 × 100 sp, 2d4 × 100 gp, 6d6 pp, lesser minor armor, greater minor wand, five grade 3 gemstones, grade 3 art object'}, {'cost': 10000, 'index': 1, 'count': 0, 'item': '10,000 gp', 'description': '4d4 × 1,000 cp, 6d6 × 100 sp, 2d4 × 100 gp, 6d6 pp, greater minor armor, lesser minor weapon, lesser minor wondrous item, greater medium scroll, grade 4 gemstone, grade 3 art object'}, {'cost': 15000, 'index': 2, 'count': 0, 'item': '15,000 gp', 'description': '2d4 × 1,000 cp, 6d4 × 100 sp, 3d6 × 10 gp, 6d6 pp, greater minor ring, two lesser minor wondrous items, two greater medium potions, greater minor wand, grade 4 gemstone, grade 3 art object'}, {'cost': 20000, 'index': 3, 'count': 0, 'item': '20,000 gp', 'description': '2d4 × 1,000 cp, 6d4 × 100 sp, 3d6 × 10 gp, 6d6 pp, greater minor armor, lesser medium rod, greater minor wondrous item, two lesser major potions, greater medium scroll, three grade 3 art objects'}, {'cost': 25000, 'index': 4, 'count': 0, 'item': '25,000 gp', 'description': '2d4 × 1,000 cp, 6d4 × 100 sp, 3d6 × 10 gp, 6d6 pp, lesser medium staff, two lesser minor wondrous items, greater medium potion, lesser medium wand, two grade 2 gemstones, two grade 3 gemstones, grade 4 gemstone'}, {'cost': 30000, 'index': 5, 'count': 0, 'item': '30,000 gp', 'description': '2d4 × 1,000 cp, 6d4 × 100 sp, 3d6 × 10 gp, 6d6 pp, lesser medium armor, greater minor weapon, lesser medium wondrous item, two lesser major scrolls, grade 4 art object'}, {'cost': 40000, 'index': 6, 'count': 0, 'item': '40,000 gp', 'description': '4d4 × 1,000 cp, 6d6 × 100 sp, 2d4 × 100 gp, 6d6 pp, lesser medium weapon, greater medium rod, greater major potion, greater medium scroll, lesser medium wand, three grade 3 art objects, two grade 4 art objects'}, {'cost': 50000, 'index': 7, 'count': 0, 'item': '50,000 gp', 'description': '4d4 × 10,000 cp, 6d6 × 1,000 sp, 4d4 × 100 gp, 2d4 × 10 pp, greater minor armor, two greater minor weapons, greater medium staff, greater minor wondrous item, grade 5 gemstone'}, {'cost': 60000, 'index': 8, 'count': 0, 'item': '60,000 gp', 'description': '2d4 × 10,000 cp, 2d4 × 1,000 sp, 2d4 × 100 gp, 2d4 × 10 pp, greater medium weapon, greater medium rod, lesser medium wondrous item, greater major scroll, two greater minor wands, grade 4 gemstone, five grade 2 art objects'}, {'cost': 75000, 'index': 9, 'count': 0, 'item': '75,000 gp', 'description': '2d4 × 10,000 cp, 2d4 × 1,000 sp, 2d4 × 100 gp, 2d4 × 10 pp, lesser major armor, greater medium ring, lesser medium staff, greater medium wand, grade 6 gemstone, grade 4 art object'}, {'cost': 100000, 'index': 10, 'count': 0, 'item': '100,000 gp', 'description': '2d4 × 10,000 cp, 2d4 × 1,000 sp, 2d4 × 100 gp, 2d4 × 10 pp, lesser medium weapon, greater medium ring, lesser major rod, greater medium wondrous item, two greater major potions, lesser medium scroll, two grade 4 art objects'}, {'cost': 125000, 'index': 11, 'count': 0, 'item': '125,000 gp', 'description': '4d4 × 10,000 cp, 6d6 × 1,000 sp, 4d4 × 100 gp, 2d8 × 10 pp, greater major armor, lesser medium weapon, lesser major staff, two greater major scrolls, greater major wand, grade 6 gemstone, three grade 4 art objects'}, {'cost': 150000, 'index': 12, 'count': 0, 'item': '150,000 gp', 'description': '4d4 × 10,000 cp, 6d6 × 1,000 sp, 4d4 × 100 gp, 2d8 × 10 pp, greater medium armor, lesser major ring, greater major wondrous item, greater major wand'}, {'cost': 200000, 'index': 13, 'count': 0, 'item': '200,000 gp', 'description': '4d4 × 10,000 cp, 6d6 × 1,000 sp, 4d4 × 100 gp, 2d8 × 10 pp, greater major weapon, two lesser medium rings, lesser major staff, lesser major wondrous item, lesser major wand, three grade 5 gemstones, grade 4 gemstone'}, {'cost': 300000, 'index': 14, 'count': 0, 'item': '300,000 gp', 'description': '8d4 × 10,000 cp, 12d6 × 1,000 sp, 8d4 × 100 gp, 2d8 × 10 pp, greater major weapon, lesser major ring, greater major staff, greater major wondrous item, greater medium wand, grade 6 gemstone, grade 6 art object'}]}"
'{"mode": "hoard_generate", "b": [{"count": 1, "item": }] }'
        ]

test_data = DATA
if len(OVERRIDE_DATA) == 0:
    test_data = OVERRIDE_DATA

for test_item in DATA:
    webgen.run_webgen(json.loads(test_item))

# And finally, a huuuuge test!
# Obtain a list of all possible treasure items.
basis = webgen.run_webgen_internal(json.loads('{"mode": "hoard_types", "type_a": "true", "type_b": "true", "type_c": "true", "type_d": "true", "type_e": "true", "type_f": "true", "type_g": "true", "type_h": "true", "type_i": "true"}'));

# This test code writes the basis to a file so it can be edited by hand.
#out = open('test.txt', 'w')
#print(basis, file=out)
#out.close()

# Update the counts of all of them by 1.
for tt in basis:
    for item in basis[tt]:
        item['count'] += 1;
# And feed that into the generator input.
basis['mode'] = "hoard_generate"

webgen.run_webgen(basis)
