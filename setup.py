"""iMoDELS """

from __future__ import print_function

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

#####################################
VERSION = "0.1.0"
ISRELEASED = False
if ISRELEASED:
    __version__ = VERSION
else:
    __version__ = VERSION + '.dev0'
#####################################

with open('imodels/version.py', 'w') as version_file:
    version_file.write('version="{0}"\n'.format(__version__))

with open('__conda_version__.txt', 'w') as conda_version:
    conda_version.write(__version__)

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open('requirements.txt') as reqs_file:
    reqs = [line.strip() for line in reqs_file]

print(reqs)

setup(
    name='imodels',
    version=__version__,
    description=__doc__.split('\n')[0],
    long_description=__doc__,
    author='Christoph Klein, Janos Sallai',
    author_email='christoph.klein@vanderbilt.edu, janos.sallai@vanderbilt.edu',
    url='https://github.com/imodels/imodels',
    download_url='https://github.com/imodels/imodels/tarball/{}'.format(__version__),
    packages=find_packages(),
    package_dir={'imodels': 'imodels'},
    include_package_data=True,
    install_requires=reqs,
    license="MIT",
    zip_safe=False,
    keywords='imodels',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
    test_suite='tests',
)
