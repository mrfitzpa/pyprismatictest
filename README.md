# PyPrismatic Test (PyPrismaticTest)

`pyprismatictest` is a Python library for quickly testing the installation of
the Python library `pyprismatic`.

## Installing `pyprismatictest`

The easiest way to install `pyprismatictest` involves using both the conda
package manager and ``pip``. While it is possible to install `pyprismatictest`
without the use of the conda package manager, it is more difficult. Because of
this, we discuss only the simplest installation procedure below.

Of course, to use the conda package manager, one must install either `anaconda3`
or `miniconda3`. For installation instructions for `anaconda3` click
[here](https://docs.anaconda.com/anaconda/install/index.html); for installation
instructions for `miniconda3`, click
[here](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/macos.html).

First, open up the appropriate command line interface. On Unix-based systems,
you would open a terminal. On Windows systems you would open an Anaconda Prompt
as an administrator.

Next, you can optionally update your conda package manager by issuing the
following command:

    conda update conda

It is recommended that you install `pyprismatictest` and its dependencies in a
virtual environment: click
[here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
for a discussion on the creation and management of conda virtual
environments. The remaining instructions assumes that you activate the conda
(virtual) environment in which you intend to install `pyprismatictest` and its
dependencies.

The first dependency that we need to install is `pyprismatic`. GPU acceleration
is available for `pyprismatic` (and thus `pyprismatictest`) if the following
conditions are met:

1. You are using a Linux or Windows machine that has NVIDIA GPUs.
2. A NVIDIA driver is installed with CUDA version 10.2.89 or greater.

If the above conditions have been met, and you would like to be able to use GPUs
with `pyprismatictest`, run the following command:

    conda install -c conda-forge pyprismatic=2.*=gpu* cudatoolkit==<X>.<Y>.*

where `<X>` and `<Y>` are the major and minor versions of CUDA installed on your
machine, e.g. CUDA version 10.2.89 has a major version of `10`, and a minor
version of `2`. Otherwise, for CPU support only, run the following command:

    conda install -c conda-forge pyprismatic=2.*=cpu*

Finally, to install `pyprismatictest`, change into the root of the repository,
and then run the following command:

    pip install .

Note that you must include the period as well.

## How to use `pyprismatictest`

`pyprismatictest` is intended as a command line tool. To use it as such, run the
following command:

    pyprismatictest

Upon doing so, `pyprismatictest` will test `pyprismatic`, and if the test
terminates without errors you should see an output message that reads:

   nFinished test of ``pyprismatic`` without errors.