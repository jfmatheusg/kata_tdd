from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTest(TestCase):
    def test_cadenaVacia(self):
        self.assertEqual(Estadisticas.getEstadisticas(""), (0, 0, 0, 0), "Cadena vacia")

    def test_cadenadeUnElemento(self):
        self.assertEqual(Estadisticas.getEstadisticas("1"), (1, 1, 1, 1), "Cadena un elemento")

    def test_cadenadeDosElementos(self):
        self.assertEqual(Estadisticas.getEstadisticas("6,4"), (2, 4, 6, 5), "Cadena dos elementos")

    def test_cadenadeNElementos(self):
        self.assertEqual(Estadisticas.getEstadisticas("3,2,8,5"), (4, 2, 8), "Cadena de 4 elementos (n)")
