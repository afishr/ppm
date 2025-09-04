from setuptools import setup
from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(
    name="ppm",
    version="0.1.0",
    description="A pip wrapper like npm",
    author="Alexandr Calugari",
    author_email="afishr00@gmail.com",
    py_modules=["ppm", "pip_tools"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "ppm = ppm:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.3',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
