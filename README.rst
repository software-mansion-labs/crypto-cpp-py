Crypto-cpp-py
=============
A python packaged `crypto-cpp <https://github.com/software-mansion-labs/crypto-cpp/tree/master>`_ library, that can be used for hashing and signing messages in starknet.


Dependencies
------------
- ecdsa,
- sympy,
- pywin32 (Windows only),
- cmake [optional, for building package from sdist; can be installed with `pip install crypto-cpp-py[build]`]

|

Changelog
=========

Version 2.0.0 (2026-04-03)
--------------------------

* Update dependencies
* Drop support for Python 3.8 and 3.9
* Add support for Python 3.13 and 3.14
* Drop support for legacy 32-bit Linux architectures

Version 1.4.5 (2024-11-20)
--------------------------

* Update `sympy <https://pypi.org/project/sympy/>`_ version to 1.12.1

Version 1.4.4 (2024-01-30)
--------------------------

* Add support for Python 3.12

Version 1.4.0 (2023-05-12)
--------------------------

* Add support for Windows

Version 1.3.1 (2023-04-27)
--------------------------

* Add support for Python 3.11

Version 1.3.0 (2023-04-20)
--------------------------

* Remove cairo-lang dependency
* Require ecdsa, sympy
