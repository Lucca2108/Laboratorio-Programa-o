import unittest
from classes import Mago, Arqueiro, Cavaleiro


class TestClasses(unittest.TestCase):

    def test_mago_criado(self):
        mago = Mago("Merlin")
        self.assertEqual(mago.nome, "Merlin")
        self.assertEqual(mago.classe, "mago")
        self.assertEqual(mago.vida, 30)

    def test_arqueiro_criado(self):
        arqueiro = Arqueiro("Legolas")
        self.assertEqual(arqueiro.classe, "arqueiro")
        self.assertEqual(arqueiro.vida, 40)

    def test_cavaleiro_espada(self):
        cavaleiro = Cavaleiro("Arthur", "espada")
        self.assertEqual(cavaleiro.arma, "espada")
        self.assertEqual(cavaleiro.bonus_dano, 2)
        
    def test_cavaleiro_criado(self):
        cavaleiro = Cavaleiro("Lancelot", "machado")
        self.assertEqual(cavaleiro.nome, "Lancelot")
        self.assertEqual(cavaleiro.classe, "cavaleiro")
        self.assertEqual(cavaleiro.vida, 55)
        self.assertEqual(cavaleiro.armadura, 50)
        self.assertEqual(cavaleiro.velocidade, 10)
        self.assertEqual(cavaleiro.ca, 16)
        self.assertEqual(cavaleiro.modificador_ataque, 5)

    def test_cavaleiro_machado(self):
        cavaleiro = Cavaleiro("Thor", "machado")
        self.assertEqual(cavaleiro.arma, "machado")
        self.assertEqual(cavaleiro.bonus_dano, 4)

    def test_cavaleiro_arma_invalida(self):
        with self.assertRaises(ValueError):
            Cavaleiro("Arthur", "lança")


if __name__ == "__main__":
    unittest.main()