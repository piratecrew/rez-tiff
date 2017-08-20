# -*- coding: utf-8 -*-

name = 'tiff'

version = '4.0.8'

authors = ['fredrik.brannbacka']

variants = [["platform-linux"]]

build_requires = [
    "jpeg",
    "zlib"
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
