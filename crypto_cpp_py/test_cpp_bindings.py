import unittest

from starkware.crypto.signature.signature import inv_mod_curve_size

from crypto_cpp_py.cpp_bindings import cpp_hash, cpp_verify, cpp_get_public_key, cpp_sign


class TestBindings(unittest.TestCase):
    def test_cpp_hash(self):
        left = 1
        right = 2

        self.assertEqual(cpp_hash(left, right), 0x5bb9440e27889a364bcb678b1f679ecd1347acdedcbf36e83494f857cc58026)

    def test_cpp_verify(self):
        r = 0x66f8955f5c4cbad5c21905ca2a968bc32a183e81069b851b7fc388eceaf57f1
        s = 0x13d5af50c934213f27a8cc5863aa304165aa886487fcc575fe6e1228879f9fe
        key = 0x7697f8f9a4c3e2b1efd882294462fda2ca9c439d02a3a04cf0a0cdb627f11ee
        msg_hash = 0x1
        w = inv_mod_curve_size(s)

        self.assertTrue(cpp_verify(msg_hash, r, w, key))
        self.assertFalse(cpp_verify(msg_hash, w, r, key))

    def test_cpp_get_public_key(self):
        private_key = 0x4070e7abfa479cf8a30d38895e93800a88862c4a65aa00e2b11495998818046
        public_key = 0x7697f8f9a4c3e2b1efd882294462fda2ca9c439d02a3a04cf0a0cdb627f11ee

        self.assertEqual(cpp_get_public_key(private_key), public_key)

    def test_cpp_sign(self):
        msg_hash = 0x052fc40e34aee86948cd47e1a0096fa67df8410f81421f314a1eb18102251a82
        private_key = 0x4070e7abfa479cf8a30d38895e93800a88862c4a65aa00e2b11495998818046

        r, s = cpp_sign(msg_hash, private_key)
        self.assertEqual(r, 0x492dd10d8b65802dcf82bdb31d8fee2f9fc24193366c674c7316e0d96920c3d)
        self.assertEqual(s, 0x65c8a1742897fb128d71e9fcc0e907fd1054bce96465410923aed7e4afede78)