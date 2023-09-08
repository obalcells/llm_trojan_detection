from setuptools import setup, find_packages

with open('requirements.txt', 'r') as requirements:
    setup(
        name='your_package_name',
        version='0.1',
        packages=find_packages(),
        description='',
        python_requires='>=3.8',
        author="Oscar Balcells",
        install_requires=list(requirements.read().splitlines()),
    )
