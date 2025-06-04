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



# The current script creates a virtual environment and installs the
# ``pyprismatictest`` library within said environment. If the script is executed
# on a Digital Alliance of Canada (DRAC) high-performance computing (HPC)
# server, then the virtual environment is created via ``virtualenv``. Otherwise,
# the virtual environment is created via ``conda``. For the latter scenario, an
# ``anaconda`` or ``miniconda`` distribution must be installed prior to running
# the script.
#
# The correct form of the command to run the script is::
#
#  source default_env_setup_for_slurm_jobs.sh <env_name> <gpu_support>
#
# where ``<env_name>`` is the path to the virtual environment, if the script is
# being executed on a DRAC HPC server, else it is the name of the ``conda``
# virtual environment; and ``<gpu_support>`` is a boolean, i.e. it should either
# be ``true`` or ``false``. If ``<gpu_support>`` is set to ``true``, then the
# GPU version of ``pyprismatic`` is installed within the environment. Otherwise,
# it is not.



# Get the path to the root of the repository.
cmd="realpath "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)""
path_to_repo_root=$(${cmd})



# Automatically determine whether the script is being executed on a DRAC HPC
# server.
current_machine_is_on_a_drac_server=false

dns_domain_name_of_current_machine=$(hostname -d)
if [ -z "${dns_domain_name_of_current_machine}" ]
then
    dns_domain_name_of_current_machine=$(hostname | grep -oP '(?<=\.).*$')
fi

readarray -t drac_dns_domain_names < ${path_to_repo_root}/drac_dns_domain_names

for drac_dns_domain_name in "${drac_dns_domain_names[@]}"
do
    if [ "${drac_dns_domain_name}" = "${dns_domain_name_of_current_machine}" ]
    then
	current_machine_is_on_a_drac_server=true
	break
    fi
done



if [ "${current_machine_is_on_a_drac_server}" = true ]
then
    # Parse the command line arguments.
    if [ $# -eq 0 ]
    then
	path_to_virtual_env=~/pyprismatictest
	install_gpu_version_of_pyprismatic=false
    else
	path_to_virtual_env=$1
	install_gpu_version_of_pyprismatic=$2
    fi



    # Load some DRAC software modules.
    source ${path_to_repo_root}/load_drac_modules.sh



    # Create the virtual environment, activate it, and then upgrade ``pip``.
    cmd="realpath "$(dirname "${path_to_virtual_env}")""
    path_to_parent_dir_of_virtual_env=$(${cmd})
    
    mkdir -p ${path_to_parent_dir_of_virtual_env}
    
    virtualenv --no-download ${path_to_virtual_env}
    source ${path_to_virtual_env}/bin/activate
    pip install --no-index --upgrade pip

    

    # Install dependencies of ``pyprismatictest``.
    if [ "${install_gpu_version_of_pyprismatic}" = true ]
    then
	pyprismatic_pkg="pyprismatic-gpu"
    else
	pyprismatic_pkg="pyprismatic-cpu"
    fi
    pkgs="h5py scipy "${pyprismatic_pkg}
    pip install --no-index ${pkgs}
else
    # Parse the command line arguments.
    if [ $# -eq 0 ]
    then
	virtual_env_name=pyprismatictest
	install_gpu_version_of_pyprismatic=false
    else
	virtual_env_name=$1
	install_gpu_version_of_pyprismatic=$2
    fi



    # Determine automatically whether NVIDIA drivers have been installed. If
    # they have been installed, then the script will install GPU-supported
    # versions of certain libraries.
    nvidia_smi_cmd_1="nvidia-smi"

    nvidia_smi_cmd_2="/c/Program\ Files/NVIDIA\ Corporation/NVSMI"
    nvidia_smi_cmd_2=${nvidia_smi_cmd_2}"/nvidia-smi.exe"

    nvidia_smi_cmd_3="/c/Windows/System32/DriverStore/FileRepository/nvdm*"
    nvidia_smi_cmd_3=${nvidia_smi_cmd_3}"/nvidia-smi.exe"

    declare -a nvidia_smi_cmds=("${nvidia_smi_cmd_1}"
				"${nvidia_smi_cmd_2}"
				"${nvidia_smi_cmd_3}")

    for nvidia_smi_cmd in "${nvidia_smi_cmds[@]}"
    do
	${nvidia_smi_cmd} 2>/dev/null
	if [ "$?" -ne 0 ]
	then
	    major_cuda_version="0"
	    continue
	fi

	cmd_seq=${nvidia_smi_cmd}
	cmd_seq=${cmd_seq}" | grep -oP '(?<=CUDA Version: )'.*"
	cmd_seq=${cmd_seq}"| grep -oP '([1-9]+)' | head -1"
	major_cuda_version="$(eval "${cmd_seq}")"

	if [ "$?" -eq 0 ]
	then
	    break
	fi
    done



    # Determine which version of ``pyprismatic`` to install.
    if [ "${major_cuda_version}" -ge 11 ]
    then
	if [ "${install_gpu_version_of_pyprismatic}" = true ]
	then
	    pyprismatic_pkg="pyprismatic=*=gpu*"
	else
	    pyprismatic_pkg="pyprismatic=*=cpu*"
	fi
    else
	pyprismatic_pkg="pyprismatic=*=cpu*"
    fi



    # Create the ``conda`` virtual environment, activate the virtual
    # environment, and then install ``pyprismatic``.
    conda create -n ${virtual_env_name} python=3.12 -y -c conda-forge
    conda activate ${virtual_env_name}
    conda install -y ${pyprismatic_pkg} -c conda-forge
fi



# Install ``pyprismatictest``.
cd ${path_to_repo_root}
pip install .
