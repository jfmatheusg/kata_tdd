
class Estadisticas:

    def getEstadisticas(cadena):
        if cadena == "":
            return (0, 0)
        elif "," in cadena:
            numeros = cadena.split(",")
            tam = 0
            minimo = numeros[0]
            for num in numeros:
                tam += 1
                if num < minimo:
                    minimo = num;
            return tam, int(minimo)
        else:
            return 1,int(cadena)
