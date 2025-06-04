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
r"""Contains tests for the root of the package :mod:`pyprismatictest`.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For operations related to unit tests.
import pytest



# For testing the installation of ``pyprismatic``.
import pyprismatictest



##################################
## Define classes and functions ##
##################################

def test_1_of_test_pyprismatic():
    pyprismatictest._test_pyprismatic()

    return None



###########################
## Define error messages ##
###########################
