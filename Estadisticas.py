
class Estadisticas:

    def getEstadisticas(cadena):
        if cadena == "":
            return 0, 0, 0, 0
        elif "," in cadena:
            num = cadena.split(",")
            tam = 0
            min = num[0]
            max = num[0]
            for num in num:
                tam += 1
                if num < min:
                    min = num
                if num > max:
                    max = num
            return tam, int(min), int(max)
        else:
            return 1, int(cadena), int(cadena), int(cadena)
