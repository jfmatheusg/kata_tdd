from unittest import TestCase

from Estadisticas import Estadisticas

class MaximoTest(TestCase):
    def test_maximocadenavacia(self):
        self.assertEqual(Estadisticas.getEstadisticas(""), 0, "Cadena vacia")

    def test_maximocadeUnElemento(self):
        self.assertEqual(Estadisticas.getEstadisticas("1"), 1, "Cadena un elemento")
