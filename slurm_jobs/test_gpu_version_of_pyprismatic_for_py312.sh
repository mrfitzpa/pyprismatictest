#!/bin/bash
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



# The current script tests Digital Research Alliance of Canada's wheel of
# ``PyPrismatic_gpu`` for Python 3.12.



#SBATCH --job-name=test_cpu_version_of_pyprismatic_for_py312
#SBATCH --nodes=1
#SBATCH --mem=4G                 # CPU memory per node
#SBATCH --cpus-per-task=1        # CPU cores/threads
#SBATCH --gpus-per-node=v100l:1  # GPU type and number of GPUs per node.
#SBATCH --time=00-00:30    # time (DD-HH:MM)
#SBATCH --mail-type=ALL

# Parse the command line arguments.
path_to_dir_containing_current_script=${1}
path_to_repo_root=${2}
path_to_data_dir_1=${3}
overwrite_slurm_tmpdir=${4}

# Get the path to the root of the repository.
path_to_dir_containing_current_script=\
$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

path_to_repo_root=$(dirname ${path_to_dir_containing_current_script})



# Setup the Python virtual environment used to execute the main action steps.
basename=custom_env_setup_for_slurm_jobs.sh
if [ ! -f ${path_to_repo_root}/${basename} ]
then
    basename=default_env_setup_for_slurm_jobs.sh
fi
source ${path_to_repo_root}/${basename} ${SLURM_TMPDIR}/tempenv true



# Run test.
pyprismatictest
python_script_exit_code=$?

if [ "${python_script_exit_code}" -ne 0 ];
then
    msg="\n\n\nThe slurm job terminated early with at least one error. "
    msg=${msg}"See traceback for details.\n\n\n"
    echo -e ${msg}
    exit 1
fi
