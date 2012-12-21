PFRPG Item Generator
Version 0.1
21 September 2012
-------------------------------------------------------------------------------

1. Identification

The PFRPG Item Generator is a tool to assist with the selection of
random items from the Pathinder Roleplaying Game.  It is intended for GMs who
wish to generate available magic items for settlements, or items found from
vanquished monsters, loot caches, and treasure hoards.  For settlement item
generation, it follows the rules laid out in the Core Rulebook and Game Mastery
Guide, with some exceptions.  For other loot generation, it follows the rules
laid out in Ultimate Equipment.  The items it generates are specified in
Ultimate Equipment.

2. Prerequisites

This software requires Python 3.x (tested with 3.0 and 3.3).

3. How to Use

In POSIX systems, there are two ways to execute Python programs.  If 
generate.py is executable, it can be run like any program, e.g.:
    $ ./generate.py
If generate.py is not executable, use chmod to make it executable, e.g.:
    $ chmod +x generate.py
Alternatively, run 'generate.py' by calling Python directly, e.g.:
    $ python generate.py
assuming 'python' is in the PATH environment variable.

On Windows systems, See http://docs.python.org/faq/windows.html for
instructions on how to run Python programs in Windows.  The remainder of this
section assumes 'generate.py' is an executable file, as known in POSIX.
For Windows, "python generate.py" should be called instead of "./generate.py",
but the command line parameters will be the same; this is the only difference
in usage.

Without parameters, generate.py simply displays instructions for usage,
although generally it is more helpful to call with the '-h' paramter, e.g.:
    $ ./generate.py -h

There are two uses of generate.py.  The first use is for generating items for
settlements.  Currently, this program only uses the Core Rulebook definitions
of settlements.  If the settlement for which you are generating items does not
match the standard definitions, generate items individually instead.

To generate items for a settlement, use the -s parameter, followed by the type
of settlement.  Settlement types made of two words, e.g. "small city" can be
entered without the space, with a dash instead of the space, or in a quoted
string, space included.  The following command lines would all work for a small
city:
    $ ./generate.py -s smallcity
    $ ./generate.py -s small-city
    $ ./ generate.py -s"small city"
    $ ./ generate.py -s="small city"

The output will have a heading, the settlement base value (for reference, if
needed), a list of minor magic items, a list of medium magic items, and a list
of major magic items, the number of which (or if any at all are generated)
are determined by the settlement size, according to Game Mastery Guide table
7-37, and are rolled by the software by default, using a pseudorandom number
generator.  You can optionally have the software prompt you for die rolls.
Add the '-m' parameter, and most automatic rolls (with some exceptions for now,
though this may change in a future version) are replaced with a prompt on
the command line for die rolls.  The software will ask you to roll a certain
number of certain types of dice, usually d4s, d6s, and d100s, and enter the
value.  Note that this can result in very many rolls, even for a small village.
If, during such a "manual" run of the program, you change your mind and wish to
have the software roll, enter "0" in to the prompt, or abort the program (e.g.
with Ctrl+C) and try again without the '-m' option.
 
Currently, the software does not reroll items that have a cost below the
settlement's base value, as directed by the Gamemastery Guide.  This will be
supported in a future version.  Additionally, the Gamemastery Guide only
specifies how many minor, medium, and major items a settlement has, but since
the software draws items from Ultimate Equipment, and Ultimate Equipment
further divides these item strengths into "lesser" and "greater", the program
arbitrarily decides between the two choices randomly.  Currently, this random
selection does not ask for a real die roll if the '-m' option is used, and does
not select between "least", "lesser", and "greater" for slotless wondrous
items.

The other way to use the random generator is to generate a single item. To
get a random item, use the '-i' parameter, followed by a quoted string
specifying the desired item strength, which is "lesser" or "greater" (and
slotless wondrous items can also have "least"), followed by "minor", "medium",
or "major", and the type of item.  The item types are 'Armor/Shield', 'Weapon',
'Potion', 'Ring', 'Rod', 'Scroll', 'Staff', 'Wand', and 'Wondrous Item'.  For
now, the type of item is case-sensitive. This will be corrected in a future
version.

Some examples are:

Lesser Minor Wondrous Item
    $ ./generate.py -i"lesser minor Wondrous Item"

Greater Medium Armor or Shield
    $ ./generate.py -i"greater medium Armor/Shield"

In the future, other modes of operation will be available, such as the
generation of treasure hoards, and generation of random coins, jewels, and art.

4. Legal

The software in this package is copyright (c) 2012, Steven Clark.  All rights
reserved, and is stated in each source code file.
See the file "LICENSE.txt" for licensing information, terms and conditions for
usage, and a DISCLAIMER OF ALL WARRANTIES.

This softare package also includes Open Game Content.  See the file "OGL.txt"
for a copy of the Open Game License and list of Open Game Content used by this
software.

All trademarks referenced herein are property of their respective holders.