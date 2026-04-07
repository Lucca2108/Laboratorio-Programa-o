import unittest
from classes import Mago, Arqueiro, Cavaleiro


class TestClasses(unittest.TestCase):

    def test_mago_criado(self):
        mago = Mago("Merlin")
        self.assertEqual(mago.nome, "Merlin")
        self.assertEqual(mago.classe, "mago")
        self.assertEqual(mago.vida, 80)

    def test_arqueiro_criado(self):
        arqueiro = Arqueiro("Legolas")
        self.assertEqual(arqueiro.classe, "arqueiro")
        self.assertEqual(arqueiro.vida, 100)

    def test_cavaleiro_espada(self):
        cavaleiro = Cavaleiro("Arthur", "espada")
        self.assertEqual(cavaleiro.arma, "espada")
        self.assertEqual(cavaleiro.bonus_dano, 2)

    def test_cavaleiro_machado(self):
        cavaleiro = Cavaleiro("Thor", "machado")
        self.assertEqual(cavaleiro.arma, "machado")
        self.assertEqual(cavaleiro.bonus_dano, 4)

    def test_cavaleiro_arma_invalida(self):
        with self.assertRaises(ValueError):
            Cavaleiro("Arthur", "lança")


if __name__ == "__main__":
    unittest.main()