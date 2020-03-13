from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTest(TestCase):
    def test_cadenaVacia(self):
        self.assertEqual(Estadisticas.getEstadisticas(""), 0, "Cadena vacia")

    def test_cadenadeunElemento(self):
        self.assertEqual(Estadisticas.getEstadisticas("1"), 1, "Cadena un elemento")
