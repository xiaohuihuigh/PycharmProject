#coding:utf-8

import sys
from Cython.Distutils import build_ext
from distutils.core import setup
from distutils.extension import Extension
from glob import glob

for filename in (set(glob('*.py'))-set(['__init__.py','setup.py'])):
    setup(cmdclass={'build_ext':build_ext},ext_modules=[Extension(filename[:-3],[filename])])

