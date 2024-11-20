import os
import subprocess

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext
from setuptools.command.build_py import build_py


class CryptoExtension(Extension):
    def __init__(self):
        self.name = "crypto_cpp"
        Extension.__init__(self, self.name, sources=[])


class BuildPy(build_py):
    def run(self):
        self.run_command("build_ext")
        return super().run()


class BuildCrypto(build_ext):
    already_built = False

    def build_extension(self, ext):
        if self.already_built:
            print("was already built, skipping...")
            return

        if os.name != "nt":
            subprocess.run("chmod a+x ./build_extension.sh", shell=True, check=True)
            subprocess.run(
                "./build_extension.sh",
                shell=True,
                check=True,
            )
        else:
            with subprocess.Popen(
                ["powershell.exe", ".\\build_extension.ps1"]
            ) as process:
                process.wait()
                if process.returncode != 0:
                    raise Exception("Build returned a non-zero code")

        self.already_built = True


with open("README.rst") as f:
    long_description = f.read()

setup(
    name="crypto_cpp_py",
    version="1.4.5",
    description="This is a packaged crypto-cpp program",
    author="Wojciech Szymczyk, Marcin Warchoł, Kamil Jankowski",
    author_email="wojciech.szymczyk@swmansion.com, marcin.warchol@swmansion.com, kamil.jankowski@swmansion.com",
    url="https://github.com/software-mansion-labs/crypto-cpp-py.git",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    install_requires=["ecdsa==0.18.0", "sympy==1.12.1", "pywin32==306; os_name=='nt'"],
    extras_require={"build": ["cmake>=3.22.4"]},
    ext_modules=[CryptoExtension()],
    cmdclass={"build_py": BuildPy, "build_ext": BuildCrypto},
    python_requires=">=3.8",
    packages=["crypto_cpp_py"],
    package_data={"crypto_cpp_py": ["../libcrypto_c_exports.*"]},
)
