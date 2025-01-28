### Modules ###

import module #Module es el nombre del archivo con la funcion (module.py)

module.sum_numbers(1,5,10)
module.printValue("Hola Python!")

from module import sum_numbers # Esto es para llamar a una funcion concreta del modulo

sum_numbers(1,5,6)

import math
print(math.pi)
from math import pi as pi_value
print(pi_value)