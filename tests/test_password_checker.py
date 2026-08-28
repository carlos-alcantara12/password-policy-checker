"""Testes do Password Policy Checker."""

import unittest

from password_checker import (
    analisar_senha,
    possui_caractere_especial,
    possui_letra_maiuscula,
    possui_letra_minuscula,
    possui_minimo,
    possui_numero,
    possui_repeticao_consecutiva,
)


class PasswordCheckerTests(unittest.TestCase):
    def test_senha_forte_atende_todos_os_criterios(self):
        resultado = analisar_senha("Estudo@2026")

        self.assertEqual(resultado["score"], 6)
        self.assertEqual(resultado["classification"], "Strong")
        self.assertEqual(resultado["recommendations"], [])

    def test_senha_curta_e_classificada_como_fraca(self):
        resultado = analisar_senha("abc")

        self.assertEqual(resultado["classification"], "Weak")
        self.assertIn("Use at least 8 characters.", resultado["recommendations"])

    def test_repeticao_de_tres_caracteres_e_identificada(self):
        self.assertTrue(possui_repeticao_consecutiva("Abc111!x"))
        self.assertFalse(possui_repeticao_consecutiva("Abc11!xy"))

    def test_senha_vazia_nao_causa_erro(self):
        resultado = analisar_senha("")

        self.assertEqual(resultado["classification"], "Weak")
        self.assertEqual(resultado["score"], 1)

    def test_funcoes_de_criterios(self):
        senha = "Projeto@9"

        self.assertTrue(possui_minimo(senha))
        self.assertTrue(possui_letra_maiuscula(senha))
        self.assertTrue(possui_letra_minuscula(senha))
        self.assertTrue(possui_numero(senha))
        self.assertTrue(possui_caractere_especial(senha))


if __name__ == "__main__":
    unittest.main()
