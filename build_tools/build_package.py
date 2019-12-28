import os
from setuptools import sandbox


def build_package(package_path):
    setup_path = f'{package_path}/setup.py'
    print(package_path)
    if os.path.exists(setup_path):
        print('*' * 80)
        print(f'Building using {setup_path}')
        sandbox.run_setup(setup_path, ['sdist', 'bdist_wheel'])
