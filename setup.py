#!/usr/bin/env python3

from distutils.core import setup
from glob import glob
from sysconfig import get_paths

setup(
    name='kufur-generator',
    version='1.2',
    description='Turkce kufur ureteci',
    author='seqizz',
    include_package_data=True,
    packages=["kufur-generator"],
    data_files=[
        ('{}/kufur-generator/data'.format(get_paths()['purelib']), glob('kufur-generator/data/*'))
    ],
)
