#!/usr/bin/env python3.3

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

        ]

OVERRIDE_DATA = [
        #'{"mode": "faiiiil"}',
        '{"mode": "hoard_budget", "type": "custom", "custom_gp":"3000"}',
        #'{"mode": "hoard_budget", "type": "encounter", "apl": 1, "rate": "slow", "magnitude": "standard"}',
        #'{"mode": "hoard_budget", "type": "encounter", "apl": 1, "rate": "medium", "magnitude": "standard"}',
        #'{"mode": "hoard_budget", "type": "encounter", "apl": 1, "rate": "fast", "magnitude": "standard"}',
        #'{"mode": "hoard_budget", "type": "encounter", "apl": 1, "rate": "medium", "magnitude": "incidental"}',
        #'{"mode": "hoard_budget", "type": "encounter", "apl": 1, "rate": "medium", "magnitude": "double"}',
        #'{"mode": "hoard_budget", "type": "encounter", "apl": 1, "rate": "medium", "magnitude": "triple"}',
        #'{"mode": "hoard_budget", "type": "npc_gear", "npc_level": 1, "heroic": "false"}',
        #'{"mode": "hoard_treasuretype", "type_a": "true", "type_b": "true"}',
        ]


if len(OVERRIDE_DATA) == 0:
    for test_item in DATA:
        webgen.run_webgen(json.loads(test_item))
else:
    for test_item in OVERRIDE_DATA:
        webgen.run_webgen(json.loads(test_item))


