from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("pyshen.primitives", ["pyshen/primitives.py"],  extra_compile_args=[]),
               Extension("pyshen.stream", ["pyshen/stream.pyx"],  extra_compile_args=[]),
               Extension("pyshen.core", ["pyshen/core.py"],  extra_compile_args=[]),
               Extension("pyshen.shen", ["pyshen/shen.py"],  extra_compile_args=["-O0"]),
               Extension("pyshen.__init__", ["pyshen/__init__.py"],  extra_compile_args=[])]

setup(
    name = 'PyShen',
    version = '0.135',
    description = 'PyShen is a port of the Shen language to Python',
    author = '',
    cmdclass = {'build_ext': build_ext},
    py_modules = ['pyshen'],
    ext_modules = ext_modules,
    long_description = ''
)
