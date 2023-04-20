import unittest

from crypto_cpp_py.cpp_bindings import (
    cpp_get_public_key,
    cpp_hash,
    cpp_sign,
    cpp_verify,
)


class TestBindings(unittest.TestCase):
    def test_cpp_hash(self):
        left = 1
        right = 2

        res = cpp_hash(left, right)
        self.assertIsInstance(res, int)
        self.assertNotEqual(res, 0)

    def test_cpp_verify(self):
        r = 0x123
        w = 0x2414
        key = 0x4141515
        msg_hash = 0x1

        res = cpp_verify(msg_hash, r, w, key)
        self.assertIsInstance(res, bool)

    def test_cpp_get_public_key(self):
        private_key = 0x1234

        res = cpp_get_public_key(private_key)
        self.assertIsInstance(res, int)
        self.assertNotEqual(res, 0)

    def test_cpp_sign(self):
        msg_hash = 0x1234
        private_key = 0x24352

        r, s = cpp_sign(msg_hash, private_key)
        self.assertIsInstance(r, int)
        self.assertNotEqual(r, 0)
        self.assertIsInstance(s, int)
        self.assertNotEqual(s, 0)
