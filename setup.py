"""A setuptools based setup module.
"""

from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

setup(
    name='wecs-mapedit',
    version='0.1.9dev',
    description='A 3D tile-based map editor for WECS and Panda3D',
    url='https://github.com/TheCheapestPixels/wecs-mapedit',
    author='janEntikan',
    author_email='janEntikan@',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=['ecs', 'wecs', 'editor', '3d', 'panda3d'],
    packages=find_packages(exclude=['tests', 'examples']),
    python_requires='>=3.7, <4',
    install_requires=[],
    extras_require={
        'wecs': ['wecs', 'cefpanda', 'panda3d'],
    },
)
