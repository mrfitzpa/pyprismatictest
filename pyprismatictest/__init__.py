# -*- coding: utf-8 -*-
# Copyright 2024 Matthew Fitzpatrick.
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.
"""``pyprismatictest`` is a Python library for quickly testing the installation
of the Python library ``pyprismatic``.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# Import child modules and packages of current package.
import pyprismatictest._sim

# Get version of current package.
from pyprismatictest.version import __version__



###############################################
## Define classes, functions, and contstants ##
###############################################

# List of public objects in package.
__all__ = []

def _test_pyprismatic():
    msg_1 = "Beginning test of ``pyprismatic``...\n\n\n"
    msg_2 = ("\n\n\nTest of ``pyprismatic`` terminated early with at least one "
             "error: see traceback for details.\n\n\n")
    msg_3 = "\n\n\nFinished test of ``pyprismatic`` without errors.\n\n\n"
    
    print(msg_1)

    try:
        pyprismatictest._sim._run_sim()
    except BaseException as err:
        print(msg_2)
        raise err

    print(msg_3)

    return None



###########################
## Define error messages ##
###########################

if __name__ == "__main__":
    _test_pyprismatic()
