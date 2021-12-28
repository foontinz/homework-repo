import os
import uuid
from betroot.lsn_10_tasks.bak_filesdir.config import cache_directory


def cache_check():
    return os.path.isdir(cache_directory)


def cache_create():
    if not cache_check():
        os.mkdir(cache_directory)


def generate_bak():
    if cache_check():
        os.chdir(cache_directory)
        with open(f'{uuid.uuid4()}.bak', 'w'):
            pass
    else:
        cache_create()
        generate_bak()


if __name__ == '__main__':

    for i in range(5):
        generate_bak()
    bak_files = [bak_file for bak_file in os.listdir(cache_directory) if bak_file.endswith('.bak')]
    for i in bak_files:
        print(i)
