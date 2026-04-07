import unittest
from funcoes import calcular_vida, esta_vivo, curar, upar_nivel, caminho


class TestJogo(unittest.TestCase):

    def test_calcular_vida(self):
        self.assertEqual(calcular_vida(10, 5), 5)

    def test_calcular_vida_zero(self):
        self.assertEqual(calcular_vida(10, 20), 0)

    def test_esta_vivo(self):
        self.assertTrue(esta_vivo(10))

    def test_esta_morto(self):
        self.assertFalse(esta_vivo(0))

    def test_curar(self):
        self.assertEqual(curar(10, 5), 15)

    def test_curar_erro(self):
        with self.assertRaises(ValueError):
            curar(10, -5)

    def test_upar(self):
        self.assertEqual(upar_nivel(1, 20), (2, 30))

    def test_upar_erro(self):
        with self.assertRaises(ValueError):
            upar_nivel(-1, 20)

    def test_caminho(self):
        self.assertIn("floresta", caminho("Floresta").lower())

    def test_caminho_erro(self):
        with self.assertRaises(ValueError):
            caminho("Praia")


if __name__ == "__main__":
    unittest.main()