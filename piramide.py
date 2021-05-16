"""
Suma numeros y los muestra en forma de piramide
"""

# menor = int(input('Ingresa el numero menor: '))
# upper = int(input('Ingresa el numero mayor: '))

def pyramid_sum(lower, upper, margin=0):
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + pyramid_sum(lower+1, upper, margin +4)
        print(blanks, result)
        return result
        
pyramid_sum(2,3)