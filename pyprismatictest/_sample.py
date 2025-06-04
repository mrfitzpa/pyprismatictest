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
r"""For modelling the sample.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For general array handling.
import numpy as np



###############################################
## Define classes, functions, and contstants ##
###############################################

def _generate_lattice_parameters_of_primitive_unit_cell_of_MoS2():
    a_MoS2 = 3.1604
    b_MoS2 = a_MoS2
    c_MoS2 = 12.295

    alpha_MoS2 = np.pi/2
    beta_MoS2 = alpha_MoS2
    gamma_MoS2 = 2*np.pi/3

    lattice_parameters_of_primitive_unit_cell_of_MoS2 = {"a": a_MoS2,
                                                         "b": b_MoS2,
                                                         "c": c_MoS2,
                                                         "alpha": alpha_MoS2,
                                                         "beta": beta_MoS2,
                                                         "gamma": gamma_MoS2}

    return lattice_parameters_of_primitive_unit_cell_of_MoS2



def _generate_lattice_vectors_orthorhombic_unit_cell_of_MoS2():
    lattice_parameters_of_primitive_unit_cell_of_MoS2 = \
        _generate_lattice_parameters_of_primitive_unit_cell_of_MoS2()

    a_MoS2 = lattice_parameters_of_primitive_unit_cell_of_MoS2["a"]
    c_MoS2 = lattice_parameters_of_primitive_unit_cell_of_MoS2["c"]

    a_MoS2_1 = a_MoS2 * np.array([1.0, 0.0, 0.0])
    a_MoS2_2 = a_MoS2 * np.array([0.0, np.sqrt(3), 0.0])
    a_MoS2_3 = c_MoS2 * np.array([0.0, 0.0, 1.0])

    lattice_vectors_orthorhombic_unit_cell_of_MoS2 = (a_MoS2_1,
                                                      a_MoS2_2,
                                                      a_MoS2_3)

    return lattice_vectors_orthorhombic_unit_cell_of_MoS2



def _generate_positions_of_S_atoms_in_orthorhombic_unit_cell_of_MoS2():
    a_MoS2_1, a_MoS2_2, a_MoS2_3 = \
        _generate_lattice_vectors_orthorhombic_unit_cell_of_MoS2()

    u = 0.612

    delta_S_1 = (1/2)*a_MoS2_1 + (1/6)*a_MoS2_2 + (u-1/2)*a_MoS2_3
    delta_S_2 = (1/2)*a_MoS2_1 + (1/6)*a_MoS2_2 + (1-u)*a_MoS2_3
    delta_S_3 = (2/3)*a_MoS2_2 + (-1/2+u)*a_MoS2_3
    delta_S_4 = (2/3)*a_MoS2_2 + (1-u)*a_MoS2_3
    delta_S_5 = (1/3)*a_MoS2_2 + u*a_MoS2_3
    delta_S_6 = (1/3)*a_MoS2_2 + (3/2-u)*a_MoS2_3
    delta_S_7 = (1/2)*a_MoS2_1 + (5/6)*a_MoS2_2 + u*a_MoS2_3
    delta_S_8 = (1/2)*a_MoS2_1 + (5/6)*a_MoS2_2 + (3/2-u)*a_MoS2_3

    positions_of_S_atoms_in_orthorhombic_unit_cell_of_MoS2 = (delta_S_1,
                                                              delta_S_2,
                                                              delta_S_3,
                                                              delta_S_4,
                                                              delta_S_5,
                                                              delta_S_6,
                                                              delta_S_7,
                                                              delta_S_8)

    return positions_of_S_atoms_in_orthorhombic_unit_cell_of_MoS2



def _generate_positions_of_Mo_atoms_in_orthorhombic_unit_cell_of_MoS2():
    a_MoS2_1, a_MoS2_2, a_MoS2_3 = \
        _generate_lattice_vectors_orthorhombic_unit_cell_of_MoS2()

    delta_Mo_1 = (1/3)*a_MoS2_2 + (1/4)*a_MoS2_3
    delta_Mo_2 = (1/2)*a_MoS2_1 + (5/6)*a_MoS2_2 + (1/4)*a_MoS2_3
    delta_Mo_3 = (1/2)*a_MoS2_1 + (1/6)*a_MoS2_2 + (3/4)*a_MoS2_3
    delta_Mo_4 = (2/3)*a_MoS2_2 + (3/4)*a_MoS2_3

    positions_of_Mo_atoms_in_orthorhombic_unit_cell_of_MoS2 = (delta_Mo_1,
                                                               delta_Mo_2,
                                                               delta_Mo_3,
                                                               delta_Mo_4)

    return positions_of_Mo_atoms_in_orthorhombic_unit_cell_of_MoS2



def _generate_num_atomic_layers():
    num_atomic_layers = 2

    return num_atomic_layers



def _generate_atomic_potential_extent():
    atomic_potential_extent = 3

    return atomic_potential_extent



def _generate_x_y_and_z_tiling_indices():
    num_y_tiles = 4
    num_x_tiles = int(np.round(num_y_tiles * np.sqrt(3)))

    num_atomic_layers = _generate_num_atomic_layers()
    
    x_tiling_indices = range(0, num_x_tiles)
    y_tiling_indices = range(0, num_y_tiles)
    z_tiling_indices = range(0, (num_atomic_layers//2)+(num_atomic_layers%2))

    x_y_and_z_tiling_indices = (x_tiling_indices,
                                y_tiling_indices,
                                z_tiling_indices)

    return x_y_and_z_tiling_indices



def _generate_global_shift():
    positions_of_S_atoms_in_orthorhombic_unit_cell_of_MoS2 = \
        _generate_positions_of_S_atoms_in_orthorhombic_unit_cell_of_MoS2()
    positions_of_Mo_atoms_in_orthorhombic_unit_cell_of_MoS2 = \
        _generate_positions_of_Mo_atoms_in_orthorhombic_unit_cell_of_MoS2()
    atomic_potential_extent = \
        _generate_atomic_potential_extent()

    global_z_shift = float("inf")
    for position in positions_of_S_atoms_in_orthorhombic_unit_cell_of_MoS2:
        x, y, z = position.tolist()
        global_z_shift = min(global_z_shift, z)
    for position in positions_of_Mo_atoms_in_orthorhombic_unit_cell_of_MoS2:
        x, y, z = position.tolist()
        global_z_shift = min(global_z_shift, z)
    global_shift = -global_z_shift + atomic_potential_extent

    global_shift = np.array((0, 0, global_z_shift))

    return global_shift



def _generate_positions_of_S_atoms_in_sample_unit_cell():
    a_MoS2_1, a_MoS2_2, a_MoS2_3 = \
        _generate_lattice_vectors_orthorhombic_unit_cell_of_MoS2()
    positions_of_S_atoms_in_orthorhombic_unit_cell_of_MoS2 = \
        _generate_positions_of_S_atoms_in_orthorhombic_unit_cell_of_MoS2()
    x_tiling_indices, y_tiling_indices, z_tiling_indices = \
        _generate_x_y_and_z_tiling_indices()
    global_shift = \
        _generate_global_shift()
    num_atomic_layers = \
        _generate_num_atomic_layers()

    position_subset_1 = positions_of_S_atoms_in_orthorhombic_unit_cell_of_MoS2

    positions_of_S_atoms_in_sample_unit_cell = tuple()

    for x_tiling_idx in x_tiling_indices:
        for y_tiling_idx in y_tiling_indices:
            for z_tiling_idx in z_tiling_indices:
                tiling_shift = (x_tiling_idx*a_MoS2_1
                                + y_tiling_idx*a_MoS2_2
                                + z_tiling_idx*a_MoS2_3)

                start = 0
                stop = 4 if (num_atomic_layers%2 == 1) else 8
                single_dim_slice = slice(start, stop)

                position_subset_2 = position_subset_1[single_dim_slice]

                position_subset_3 = tuple(delta_S+global_shift+tiling_shift
                                          for delta_S
                                          in position_subset_2)

                for position in position_subset_3:
                    x, y, z = position.tolist()
                    positions_of_S_atoms_in_sample_unit_cell += ((x, y, z),)

    return positions_of_S_atoms_in_sample_unit_cell



def _generate_positions_of_Mo_atoms_in_sample_unit_cell():
    a_MoS2_1, a_MoS2_2, a_MoS2_3 = \
        _generate_lattice_vectors_orthorhombic_unit_cell_of_MoS2()
    positions_of_Mo_atoms_in_orthorhombic_unit_cell_of_MoS2 = \
        _generate_positions_of_Mo_atoms_in_orthorhombic_unit_cell_of_MoS2()
    x_tiling_indices, y_tiling_indices, z_tiling_indices = \
        _generate_x_y_and_z_tiling_indices()
    global_shift = \
        _generate_global_shift()
    num_atomic_layers = \
        _generate_num_atomic_layers()

    position_subset_1 = positions_of_Mo_atoms_in_orthorhombic_unit_cell_of_MoS2

    positions_of_Mo_atoms_in_sample_unit_cell = tuple()

    for x_tiling_idx in x_tiling_indices:
        for y_tiling_idx in y_tiling_indices:
            for z_tiling_idx in z_tiling_indices:
                tiling_shift = (x_tiling_idx*a_MoS2_1
                                + y_tiling_idx*a_MoS2_2
                                + z_tiling_idx*a_MoS2_3)

                start = 0
                stop = 2 if (num_atomic_layers%2 == 1) else 4
                single_dim_slice = slice(start, stop)

                position_subset_2 = position_subset_1[single_dim_slice]

                position_subset_3 = tuple(delta_Mo+global_shift+tiling_shift
                                          for delta_Mo
                                          in position_subset_2)

                for position in position_subset_3:
                    x, y, z = position.tolist()
                    positions_of_Mo_atoms_in_sample_unit_cell += ((x, y, z),)

    return positions_of_Mo_atoms_in_sample_unit_cell



def _calc_Delta_Z():
    a_MoS2_1, a_MoS2_2, a_MoS2_3 = \
        _generate_lattice_vectors_orthorhombic_unit_cell_of_MoS2()
    positions_of_S_atoms_in_orthorhombic_unit_cell_of_MoS2 = \
        _generate_positions_of_S_atoms_in_orthorhombic_unit_cell_of_MoS2()
    positions_of_Mo_atoms_in_orthorhombic_unit_cell_of_MoS2 = \
        _generate_positions_of_Mo_atoms_in_orthorhombic_unit_cell_of_MoS2()
    x_tiling_indices, y_tiling_indices, z_tiling_indices = \
        _generate_x_y_and_z_tiling_indices()
    atomic_potential_extent = \
        _generate_atomic_potential_extent()
    global_shift = \
        _generate_global_shift()
    num_atomic_layers = \
        _generate_num_atomic_layers()

    position_subset_1 = positions_of_S_atoms_in_orthorhombic_unit_cell_of_MoS2
    position_subset_2 = positions_of_Mo_atoms_in_orthorhombic_unit_cell_of_MoS2

    start = 0
    stop = 4 if (num_atomic_layers%2 == 1) else 8
    single_dim_slice = slice(start, stop)

    position_subset_3 = position_subset_1[single_dim_slice]

    stop = stop//2
    single_dim_slice_2 = slice(start, stop)
    position_subset_4 = position_subset_2[single_dim_slice]

    position_subset_5 = position_subset_3 + position_subset_4

    Delta_Z = -float("inf")
    for position in position_subset_5:
        x, y, z = position.tolist()
        Delta_Z = max(Delta_Z, z)
    Delta_Z += (global_shift[2].item()
                + z_tiling_indices[-1]*a_MoS2_3[2].item()
                + atomic_potential_extent)

    return Delta_Z



def _calc_sample_unit_cell_dims():
    a_MoS2_1, a_MoS2_2, a_MoS2_3 = \
        _generate_lattice_vectors_orthorhombic_unit_cell_of_MoS2()
    x_tiling_indices, y_tiling_indices, z_tiling_indices = \
        _generate_x_y_and_z_tiling_indices()

    Delta_X = len(x_tiling_indices)*np.linalg.norm(a_MoS2_1).item()
    Delta_Y = len(y_tiling_indices)*np.linalg.norm(a_MoS2_2).item()
    Delta_Z = _calc_Delta_Z()

    sample_unit_cell_dims = (Delta_X, Delta_Y, Delta_Z)

    return sample_unit_cell_dims



def _generate_atomic_coords_filename():
    atomic_coords_filename = "_temp_atomic_coords_filename.xyz"

    return atomic_coords_filename



def _generate_atomic_coords_file():
    output_filename = _generate_atomic_coords_filename()
    sample_unit_cell_dims = _calc_sample_unit_cell_dims()

    positions_of_S_atoms_in_sample_unit_cell = \
        _generate_positions_of_S_atoms_in_sample_unit_cell()
    positions_of_Mo_atoms_in_sample_unit_cell = \
        _generate_positions_of_Mo_atoms_in_sample_unit_cell()

    with open(output_filename, "w") as file_obj:
        line = "Bilayer MoS2 Sample\n"
        file_obj.write(line)

        unformatted_line = "\t{:18.14f}\t{:18.14f}\t{:18.14f}\n"
        line = unformatted_line.format(*sample_unit_cell_dims)
        file_obj.write(line)

        occ = 1  # Number is essentially not used in simulations.
    
        Z = 42  # Atomic number of Mo.

        # The RMS x-displacement of Mo atoms at room temperature. Value was
        # taken from experimental data for the RMS of the in-plane displacement
        # in Schönfeld et al., Acta Cryst. B39, 404-407 (1983).
        u_x_rms = 0.069

        for position in positions_of_Mo_atoms_in_sample_unit_cell:
            x, y, z = position
            unformatted_line = ("{}\t{:18.14f}\t{:18.14f}"
                                "\t{:18.14f}\t{:18.14f}\t{:18.14f}\n")
            line = unformatted_line.format(Z, x, y, z, occ, u_x_rms)
            file_obj.write(line)

        Z = 16  # Atomic number of S.

        # The RMS x-displacement of S atoms at room temperature. Value was taken
        # from experimental data for the RMS of the in-plane displacement in
        # Schönfeld et al., Acta Cryst. B39, 404-407 (1983).
        u_x_rms = 0.062

        for position in positions_of_S_atoms_in_sample_unit_cell:
            x, y, z = position
            unformatted_line = ("{}\t{:18.14f}\t{:18.14f}"
                                "\t{:18.14f}\t{:18.14f}\t{:18.14f}\n")
            line = unformatted_line.format(Z, x, y, z, occ, u_x_rms)
            file_obj.write(line)

        file_obj.write("-1")

    return None



def _calc_sample_supercell_lateral_pixel_size():
    Delta_X, Delta_Y, Delta_Z = _calc_sample_unit_cell_dims()
    
    sample_supercell_xy_dims_in_pixels = 2*(4*32,)
    N_x, N_y = sample_supercell_xy_dims_in_pixels

    sample_supercell_lateral_pixel_size = (Delta_X/N_x, Delta_Y/N_y)

    return sample_supercell_lateral_pixel_size



def _calc_sample_supercell_slice_thickness():
    Delta_X, Delta_Y, Delta_Z = _calc_sample_unit_cell_dims()
    
    num_sample_supercell_slices = 2

    sample_supercell_slice_thickness = Delta_Z/num_sample_supercell_slices

    return sample_supercell_slice_thickness



###########################
## Define error messages ##
###########################
