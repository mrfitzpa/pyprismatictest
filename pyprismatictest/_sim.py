# -*- coding: utf-8 -*-
# Copyright 2025 Matthew Fitzpatrick.
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
r"""For running simulations.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For performing operations on file and directory paths.
import pathlib



# For modelling the sample.
import pyprismatictest._sample

# For setting the simulation parameters.
import pyprismatictest._params



# For creating a :obj:`pyprismatic.Metadata` object that is responsible for
# running the ``prismatic`` simulation.
import pyprismatic



###############################################
## Define classes, functions, and contstants ##
###############################################

def _run_sim():
    pyprismatictest._sample._generate_atomic_coords_file()

    pyprismatic_sim_obj = pyprismatic.Metadata()
    pyprismatictest._params._update_sim_params(pyprismatic_sim_obj)
    pyprismatic_sim_obj.go()

    filenames = ("scratch_param.txt",
                 "prismatic_scratch.h5",
                 pyprismatic_sim_obj.filenameAtoms,
                 pyprismatic_sim_obj.filenameOutput)

    for filename in filenames:
        pathlib.Path(filename).unlink(missing_ok=True)

    return None



###########################
## Define error messages ##
###########################
