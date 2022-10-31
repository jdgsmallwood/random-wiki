from setuptools import setup

setup(
    name="random-wiki",
    version="1.0",
    install_requires=[
        "requests",
        "bs4",
    ],
    extras_require={
        "dev": [
            "black",
            "isort",
            "pyright",
            "pytest",
            "pytest-cov",
            "pycln",
            "pre-commit",
            "flake8",
        ]
    },
)
