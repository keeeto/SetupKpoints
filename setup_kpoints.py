from __future__ import print_function
import seekpath
import ase
import ase.io as io
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-f", "--input",
                  action="store", type="string", dest="input_file", default="POSCAR",
                  help="The crystal structure. Default POSCAR")
parser.add_option("-o", "--output",
                  action="store", type="string", dest="output_file", default="KPOINTS.k_path",
                  help="The file to which the new kpoints will be appended. Default: KPOINTS.k_path.")
parser.add_option("-r", "--resolution",
                  action="store", type="float", dest="resolution", default=0.1,
                  help="a reference target distance between neighboring k-points in the path, in units of 1/ang.")
(options, args) = parser.parse_args()

structure = io.read(options.input_file)
numbers = structure.get_atomic_numbers()
inp = (structure.cell,structure.get_scaled_positions(),numbers)

explicit_data = seekpath.get_explicit_k_path(inp,reference_distance=options.resolution)

kpath = explicit_data['explicit_kpoints_rel']

weight = 0.
with open(options.output_file,'a') as outfile:
    for point in kpath:
        outfile.write("%8.6f %8.6f %8.6f %5.3f\n" % (point[0],  point[1], point[2], weight))

print('Output written to {}'.format(options.output_file))

# Write new conventions cell, to ensure compliance with the kpoints
new_data = seekpath.get_path(inp)

new_cell = ase.Atoms(positions=new_data['conv_positions'],cell=new_data['conv_lattice'],pbc=[True,True,True])
new_cell.set_scaled_positions(new_data['conv_positions'])
new_cell.set_atomic_numbers(new_data['conv_types'])

print('New coordinates written to CONTCAR.conventional')
io.write('CONTCAR.conventional',new_cell)

