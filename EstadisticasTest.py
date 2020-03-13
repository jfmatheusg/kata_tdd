from unittest import TestCase

from Estadisticas import Estadisticas

class MaximoTest(TestCase):
    def test_maximocadenavacia(self):
        self.assertEqual(Estadisticas.maximo(""), 0, "Cadena vacia")
