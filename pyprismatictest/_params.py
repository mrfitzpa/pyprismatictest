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
r"""For setting the simulation parameters.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For modelling the sample.
import pyprismatictest._sample



###############################################
## Define classes, functions, and contstants ##
###############################################

def _update_sim_params(pyprismatic_sim_obj):
    _update_sample_model_params(pyprismatic_sim_obj)
    _update_probe_model_params(pyprismatic_sim_obj)
    _update_tilt_params(pyprismatic_sim_obj)
    _update_scan_config_params(pyprismatic_sim_obj)
    _update_output_params(pyprismatic_sim_obj)
    _update_worker_params(pyprismatic_sim_obj)
    pyprismatic_sim_obj.algorithm = "hrtem"

    return None



def _update_sample_model_params(pyprismatic_sim_obj):
    _update_discretization_params(pyprismatic_sim_obj)
    _update_thermal_params(pyprismatic_sim_obj)

    atomic_coords_filename = \
        pyprismatictest._sample._generate_atomic_coords_filename()
    atomic_potential_extent = \
        pyprismatictest._sample._generate_atomic_potential_extent()

    pyprismatic_sim_obj.includeOccupancy = False
    pyprismatic_sim_obj.importPath = ""  # Ignored.
    pyprismatic_sim_obj.importPotential = False
    pyprismatic_sim_obj.importSMatrix = False
    pyprismatic_sim_obj.importFile = ""
    pyprismatic_sim_obj.filenameAtoms = atomic_coords_filename

    pyprismatic_sim_obj.tileX = 1
    pyprismatic_sim_obj.tileY = 1
    pyprismatic_sim_obj.tileZ = 1

    pyprismatic_sim_obj.potBound = atomic_potential_extent

    return None



def _update_discretization_params(pyprismatic_sim_obj):
    atomic_coords_filename = \
        pyprismatictest._sample._generate_atomic_coords_filename()
    sample_supercell_lateral_pixel_size = \
        pyprismatictest._sample._calc_sample_supercell_lateral_pixel_size()
    sample_supercell_slice_thickness = \
        pyprismatictest._sample._calc_sample_supercell_slice_thickness()

    pyprismatic_sim_obj.realspacePixelSizeX = \
        sample_supercell_lateral_pixel_size[0]
    pyprismatic_sim_obj.realspacePixelSizeY = \
        sample_supercell_lateral_pixel_size[1]
    pyprismatic_sim_obj.sliceThickness = \
        sample_supercell_slice_thickness

    pyprismatic_sim_obj.zSampling = 16
    pyprismatic_sim_obj.potential3D = True

    pyprismatic_sim_obj.interpolationFactorX = 1
    pyprismatic_sim_obj.interpolationFactorY = 1

    return None



def _update_thermal_params(pyprismatic_sim_obj):
    pyprismatic_sim_obj.numFP = 2
    pyprismatic_sim_obj.randomSeed = 1
    pyprismatic_sim_obj.includeThermalEffects = True

    return None



def _update_probe_model_params(pyprismatic_sim_obj):
    _update_gun_model_params(pyprismatic_sim_obj)
    _update_lens_model_params(pyprismatic_sim_obj)

    pyprismatic_sim_obj.probeSemiangle = 15
    pyprismatic_sim_obj.alphaBeamMax = 24  # Ignored.

    return None



def _update_gun_model_params(pyprismatic_sim_obj):
    pyprismatic_sim_obj.E0 = 200

    return None



def _update_lens_model_params(pyprismatic_sim_obj):
    pyprismatic_sim_obj.probeDefocus = 10

    pyprismatic_sim_obj.probeDefocus_min = 0.0  # Ignored.
    pyprismatic_sim_obj.probeDefocus_max = 0.0  # Ignored.
    pyprismatic_sim_obj.probeDefocus_step = 0.0  # Ignored.
    pyprismatic_sim_obj.probeDefocus_sigma = 0.0  # Ignored.

    pyprismatic_sim_obj.C3 = 20
    pyprismatic_sim_obj.C5 = float("NaN")  # Ignored.

    pyprismatic_sim_obj.aberrations_file = ""

    return None



def _update_tilt_params(pyprismatic_sim_obj):
    pyprismatic_sim_obj.xTiltStep = 0.0
    pyprismatic_sim_obj.yTiltStep = 0.0

    pyprismatic_sim_obj.probeXtilt = 0.0
    pyprismatic_sim_obj.probeYtilt = 0.0

    pyprismatic_sim_obj.xTiltOffset = 0
    pyprismatic_sim_obj.yTiltOffset = 0

    return None



def _update_scan_config_params(pyprismatic_sim_obj):
    pyprismatic_sim_obj.probes_file = ""

    pyprismatic_sim_obj.scanWindowXMin = 0.5
    pyprismatic_sim_obj.scanWindowXMax = 0.5+1.0e-14
    pyprismatic_sim_obj.scanWindowYMin = 0.5
    pyprismatic_sim_obj.scanWindowYMax = 0.5+1.0e-14
    pyprismatic_sim_obj.scanWindowXMin_r = 0.0  # Ignored.
    pyprismatic_sim_obj.scanWindowXMax_r = 0.0  # Ignored.
    pyprismatic_sim_obj.scanWindowYMin_r = 0.0  # Ignored.
    pyprismatic_sim_obj.scanWindowYMax_r = 0.0  # Ignored.

    pyprismatic_sim_obj.probeStepX = 0.25
    pyprismatic_sim_obj.probeStepY = 0.25
    
    pyprismatic_sim_obj.nyquistSampling = False  # Ignored.

    return None



def _update_output_params(pyprismatic_sim_obj):
    pyprismatic_sim_obj.numSlices = 0
    pyprismatic_sim_obj.zStart = 0.0

    pyprismatic_sim_obj.algorithm = "multislice"
    pyprismatic_sim_obj.matrixRefocus = False

    pyprismatic_sim_obj.save2DOutput = False  # Ignored.
    pyprismatic_sim_obj.save3DOutput = False  # Ignored.
    pyprismatic_sim_obj.save4DOutput = False
    pyprismatic_sim_obj.saveDPC_CoM = False  # Ignored.
    pyprismatic_sim_obj.savePotentialSlices = False
    pyprismatic_sim_obj.saveSMatrix = False
    pyprismatic_sim_obj.saveComplexOutputWave = True
    pyprismatic_sim_obj.saveProbe = 0  # Ignored.

    pyprismatic_sim_obj.integrationAngleMin = 0  # Ignored.
    pyprismatic_sim_obj.integrationAngleMax = 1.0  # Ignored.
    pyprismatic_sim_obj.detectorAngleStep = 1.0  # Ignored.
    
    pyprismatic_sim_obj.crop4DOutput = False  # Ignored.
    pyprismatic_sim_obj.crop4Damax = 100.0  # Ignored.

    pyprismatic_sim_obj.maxFileSize = 300*10**9
    pyprismatic_sim_obj.filenameOutput = "prismatic_output.h5"

    return None


def _update_worker_params(pyprismatic_sim_obj):
    _update_cpu_params(pyprismatic_sim_obj)
    _update_gpu_params(pyprismatic_sim_obj)

    return None



def _update_cpu_params(pyprismatic_sim_obj):
    pyprismatic_sim_obj.alsoDoCPUWork = True
    pyprismatic_sim_obj.numThreads = 12
    pyprismatic_sim_obj.batchSizeTargetCPU = 1
    pyprismatic_sim_obj.earlyCPUStopCount = 100
    pyprismatic_sim_obj.batchSizeCPU = 1  # Ignored.

    return None



def _update_gpu_params(pyprismatic_sim_obj):
    pyprismatic_sim_obj.numGPUs = 4
    pyprismatic_sim_obj.batchSizeTargetGPU = 1
    pyprismatic_sim_obj.numStreamsPerGPU = 3
    pyprismatic_sim_obj.transferMode = "auto"
    pyprismatic_sim_obj.batchSizeGPU = 1  # Ignored.

    return None



###########################
## Define error messages ##
###########################
