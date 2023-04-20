import unittest

from crypto_cpp_py.utils import (
    cpp_div_mod,
    cpp_generate_k_rfc6979,
    cpp_inv_mod_curve_size,
)


class TestUtils(unittest.TestCase):
    def test_cpp_div_mod(self):
        n, m, p = 0x1, 0x2, 0x3

        res = cpp_div_mod(n, m, p)
        self.assertIsInstance(res, int)
        self.assertNotEqual(res, 0)

    def test_cpp_inv_mod_curve_size(self):
        x = 0x123

        res = cpp_inv_mod_curve_size(x)
        self.assertIsInstance(res, int)
        self.assertNotEqual(res, 0)

    def test_cpp_generate_k_rfc6979(self):
        msg_hash = 0x123
        priv_key = 0x321
        seeds = [None, 0x45]

        for seed in seeds:
            res = cpp_generate_k_rfc6979(msg_hash, priv_key, seed)
            self.assertIsInstance(res, int)
            self.assertNotEqual(res, 0)
