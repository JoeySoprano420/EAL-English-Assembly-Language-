from setuptools import setup, find_packages

setup(
    name='EAL-Project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'antlr4-python3-runtime',
        'ply',
    ],
    entry_points={
        'console_scripts': [
            'eal=eal.interpreter:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
