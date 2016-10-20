# SetupKpoints


This script uses the SeeKpath and ASE codes to take an input crystal structure and return a standardised k-path through the Brillouin zone. The path is chose *based on crystallography*.

If you do use this code you will require
* [SeeKpath](https://github.com/giovannipizzi/seekpath)
* [ASE](https://wiki.fysik.dtu.dk/ase/about.html)

If you do use it to generate the points **always remember** to cite the paper that details the process of SeeKpath :
* [Y. Hinuma, G. Pizzi, Y. Kumagai, F. Oba, I. Tanaka, Band structure diagram paths based on crystallography, arXiv:1602.06402 (2016)](https://arxiv.org/abs/1602.06402)
* [spglib](http://atztogo.github.io/spglib/index.html)


# Use
`python setup_kpoints.py [options]`

Options:
  -h, --help            show this help message and exit
  
  -f INPUT_FILE, --input=INPUT_FILE
                        The crystal structure. Default POSCAR
                        
  -o OUTPUT_FILE, --output=OUTPUT_FILE
                        The file to which the new kpoints will be appended.
                        Default: KPOINTS.k_path.
                        
  -r RESOLUTION, --resolution=RESOLUTION
                        a reference target distance between neighboring
                        k-points in the path, in units of 1/ang.
                        
  -t                    Turns off time reversal symmetry, if it is off and
                        there is no centrosymmetry, additional lines are
                        needed.                    

Example: 

`python setup_kpoints.py -f GaN.cif -o KPTS -r 0.1`

# Notes

If obtaining `SeeKpath` using `pip` make sure that you are using `Python 2`. Although `pip3 install seekpath` will work, it does not support `Python 3`.
