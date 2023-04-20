import unittest

from crypto_cpp_py.utils import (
    cpp_div_mod,
    cpp_generate_k_rfc6979,
    cpp_inv_mod_curve_size,
)


class TestUtils(unittest.TestCase):
    def test_cpp_div_mod(self):
        n, m, p = 0x13, 0x23, 0x34

        res = cpp_div_mod(n, m, p)
        self.assertIsInstance(res, int)
        self.assertEqual(res, 5)

    def test_cpp_inv_mod_curve_size(self):
        x = 0x123

        res = cpp_inv_mod_curve_size(x)
        self.assertIsInstance(res, int)
        self.assertEqual(
            res, 0x4AC6D15FE3D94B65B7DCCF9D7885B7DA29FDB42C778665757421DB07C6402DD
        )

    def test_cpp_generate_k_rfc6979(self):
        msg_hash = 0x123
        priv_key = 0x321
        seeds = [None, 0x45]
        expected = [
            0xAEBC25D7EB7ACBE836B9D0E02EE4A08678DD5FE893F3129E839B3B2E587F71,
            0x731807F737507B58A55880C2F4799FDD018F93C83BCB1787C8B5C4D29058E15,
        ]

        for seed, expected_res in zip(seeds, expected):
            res = cpp_generate_k_rfc6979(msg_hash, priv_key, seed)
            self.assertIsInstance(res, int)
            self.assertEqual(res, expected_res)
