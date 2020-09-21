#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from typing import List


def convert_to_absolute() -> float:
    nombre_in = input("entre un nombre")
    nombre = float(nombre_in)
    convert_to_absolute = math.fabs(nombre)
    print (convert_to_absolute)
    return 


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOPQ', 'ack'
    liste_de_noms = []
    for I in prefixes:
        print(I + suffixes)
        liste_de_noms.append(I+suffixes)         
    return liste_de_noms


def prime_integer_summation() -> int:   
    i=2
    primes=[]
    
    while len(primes) < 100:
        prime = True

        for divider in range(2, int(math.sqrt(i))+1):
            if i % divider == 0:
                prime = False
        if prime:
            primes.append(i)
        i+=1
    return sum(primes)


def factorial(number: int) -> int:
    our_number = float(number)
    return math.factorial(our_number)


def use_continue() -> None:
    for i in range(1,11):
        if i == 5:
            continue
        print(i, end=" ")
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme 100 premiers nombres entiers est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
