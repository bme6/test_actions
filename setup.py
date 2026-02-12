# -*- coding: utf-8 -*-
# @Time    : 2025-07-24 16:49
# @Author  : luyi
import os
import subprocess
import sys
from setuptools import find_packages, setup

def build_with_nuitka():
    """使用 Nuitka 编译模块为 C 扩展"""
    if not os.path.exists('build'):
        os.makedirs('build')

    package_dir = 'test_actions'
    for filename in os.listdir(package_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            output_name = f"{package_dir}.{module_name}"

            print(f"Compiling {filename} with Nuitka...")

            cmd = [
                sys.executable, '-m', 'nuitka',
                '--module',
                f'--output-dir=build',
                '--include-package-data',
                '--follow-imports',
                f'--python-flag=no_site,no_asserts,no_docstrings',
                output_name
            ]

            if sys.platform == 'darwin':
                cmd.append('--macos-create-bundle')

            try:
                subprocess.check_call(cmd)
            except subprocess.CalledProcessError as e:
                print(f"Warning: Failed to compile {filename}: {e}")

setup(
    name="test_actions",
    version="0.0.7",
    author="ly",
    author_email="2662017230@qq.com",
    description="my utils",
    url="https://github.com/bme6/utox",
    packages=find_packages(),
    package_dir={"test_actions": "test_actions"},
    include_package_data=True,
    package_data={
        "test_actions": ["*.so", "*.pyd", "*.pyi"],
    },
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
    ],
    install_requires=[
        "nuitka>=1.0.0",
    ],
    extras_require={
        "dev": [
            "build>=1.0.0",
            "cibuildwheel>=2.16.0",
            "setuptools>=69.0.0",
            "wheel",
        ],
        "test": [
            "pytest>=7.4.0",
        ],
    },
    zip_safe=False,
)
