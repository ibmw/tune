from pathlib import Path

from setuptools import find_namespace_packages, setup

setup(
    name="tune",
    version="1.0.1",
    description="Benchmarking HF",
    install_requires=Path("requirements.txt").read_text().splitlines(),
    packages=find_namespace_packages(include=["src.*"]),
    include_package_data=False,
    extras_require={"dev": Path("requirements-dev.txt").read_text().splitlines()},
    entry_points={
        "console_scripts": ["benchmark=launcher:main"],
    },
)
