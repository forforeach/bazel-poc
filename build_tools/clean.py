import os
import glob
import shutil



def remove_subdirs_by_path(path):
    for subdir_path in glob.iglob(path, recursive=False):
        print(f'\tRemoving {subdir_path}')
        shutil.rmtree(subdir_path)


def clean(rootdir, dirname):
    dirs_to_clean = ['/*.egg-info', '/build', '/temp', '/dist']
    for dir_path in glob.iglob(rootdir, recursive=False):
        if os.path.isdir(dir_path):
            sdk_dir_path = os.path.join(dir_path, dirname)
            print('*' * 80)
            print(f'Cleaning {sdk_dir_path}')
            for dir_to_clean in dirs_to_clean:
                remove_subdirs_by_path(f'{sdk_dir_path}{dir_to_clean}')

