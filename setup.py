"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path
from os.path import join

from toolkit.setuptools_helpers import get_L_data_dir

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='iso_tools',
    version='0.1.0',
    description='ISO 639-related language data tools',
    long_description=long_description,
    url='https://github.com/jiyiiy/iso_tools',
    author='David Morrissey',
    author_email='david.l.morrissey@gmail.com',

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Localization',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Text Processing :: General',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
    ],

    keywords='unicode',
    packages=find_packages(),

    install_requires=[
        'xmltodict',
    ],

    data_files=get_L_data_dir('iso_tools/data'),
    zip_safe=False
)
