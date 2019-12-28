import os
import glob
import argparse

import twine

from build_package import build_package
from clean import clean

parser = argparse.ArgumentParser(description='Clean packages directories')
parser.add_argument('-r', '--root', type=str,
                    help='a path to the root directory of the packages', required=True)
parser.add_argument('-dn', '--dirname', type=str,
                    help='a packages\' directory name', required=True)
parser.add_argument('-c', '--clean', type=bool,
                    help='specify if you want to clean build dirs before', default=True)

args = parser.parse_args()

rootdir = os.path.join(os.getcwd(), args.root)


for dir_path in glob.iglob(rootdir, recursive=False):
    if os.path.isdir(dir_path):
        package_path = os.path.join(dir_path, args.dirname)
        if args.clean:
            clean(package_path)
        build_package(package_path)

