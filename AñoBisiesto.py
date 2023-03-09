# E5 Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
def esBisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:  #   si es div por 100 pero no por 400 es bisiesto
            if año % 400 == 0: # T   bisiesto
                return True    # si no es div por 100 o 400 es bisiesto
            else:
                return False
        else:
            return True
    else:
        return False
    
print(esBisiesto(2020))  # True
print(esBisiesto(2021))  # False
print(esBisiesto(2022))  # False
print(esBisiesto(2023))  # False
print(esBisiesto(2024))  # True