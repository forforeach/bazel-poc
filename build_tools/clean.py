import os
import glob
import shutil



def remove_subdirs_by_path(path):
    for subdir_path in glob.iglob(path, recursive=False):
        print(f'\tRemoving {subdir_path}')
        shutil.rmtree(subdir_path)


def clean(dirpath):
    dirs_to_clean = ['/*.egg-info', '/build', '/temp', '/dist']
    print('*' * 80)
    print(f'Cleaning {dirpath}')
    for dir_to_clean in dirs_to_clean:
        remove_subdirs_by_path(f'{dirpath}{dir_to_clean}')

