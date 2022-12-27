from setuptools import setup, find_packages

setup(
    name='aoc_solutions',
    version='0.1',
    author='bernikr',
    install_requires=[
        "advent-of-code-data >= 0.8.0",
    ],
    packages=find_packages(),
    entry_points={
        "adventofcode.user": ["bernikr = entrypoint:solve"],
    },
)
