
class Estadisticas:

    def getEstadisticas(cadena):
        if cadena == "":
            return 0
        elif "," in cadena:
            return 2
        else:
            return 1
