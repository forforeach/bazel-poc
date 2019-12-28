import os
import glob
import argparse
from setuptools import sandbox

from clean import clean

parser = argparse.ArgumentParser(description='Clean packages directories')
parser.add_argument('-r', '--root', type=str,
                    help='a path to the root directory of the packages', required=True)
parser.add_argument('-dn', '--dirname', type=str,
                    help='a packages\' directory name', required=True)
parser.add_argument('-c', '--clean', type=bool, help='specify if you want to clean build dirs before', default=True)

args = parser.parse_args()

rootdir = os.path.join(os.getcwd(), args.root)

if args.clean:
    clean(rootdir, args.dirname)


for dir_path in glob.iglob(rootdir, recursive=False):
    if os.path.isdir(dir_path):
        package_path = os.path.join(dir_path, args.dirname)
        setup_path = f'{package_path}/setup.py'
        print(package_path)
        if os.path.exists(setup_path):
            print('*' * 80)
            print(f'Building using {setup_path}')
            sandbox.run_setup(setup_path, ['sdist', 'bdist_wheel'])
