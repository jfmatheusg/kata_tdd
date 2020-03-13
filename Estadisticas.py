
class Estadisticas:

    def getEstadisticas(cadena):
        if cadena == "":
            return 0
        elif "," in cadena:
            numeros = cadena.split(",")
            suma = 0
            for num in numeros:
                suma += 1
            return suma
        else:
            return 1
