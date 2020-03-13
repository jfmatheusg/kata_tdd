
class Estadisticas:

    def getEstadisticas(cadena):
        if cadena == "":
            return 0, 0, 0
        elif "," in cadena:
            num = cadena.split(",")
            tam = 0
            min = num[0]
            for num in num:
                tam += 1
                if num < min:
                    min = num;
            return tam, int(min)
        else:
            return 1,int(cadena)
