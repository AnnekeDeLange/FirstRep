__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
from shutil import rmtree
from zipfile import ZipFile


def clean_cache():
    current_dir = os.getcwd().lower()
    cache = f'{current_dir}/cache'
    if not os.path.isdir(cache):
        os.mkdir(cache)
    else:
        rmtree(cache)
        os.mkdir(cache)
    return None


# clean_cache()


def cache_zip(path_zip_file, path_cache_dir):
    dir_to_clean_cache_from = f'{path_cache_dir}/..'
    os.chdir(dir_to_clean_cache_from)
    clean_cache()
    ZipFile.extractall(ZipFile(path_zip_file), path=path_cache_dir)
    return None


# cache_zip(
#     'C://Users/Anneke/project1/files/data.zip',
#     'C://Users/Anneke/project1/files/cache')


def cached_files():
    cache_dir = f'{os.path.dirname(__file__)}/cache'
    # file_list will contain all names of all files in directory cache with absolute path
    file_list = [os.path.abspath(os.path.join(cache_dir, file)) for file in os.listdir(cache_dir)]
    return file_list


# print(cached_files())


def find_password(file_list):
    password_indicator = 'password: '
    password = ''
    while password == '':
        for f in file_list:
            with open(f) as text_file:
                file_content = text_file.read()
            if file_content.find(password_indicator) == -1:
                continue
            else:
                password_start = file_content.find(password_indicator) + len(password_indicator)
                password_end_indicators = [' ', '\n', '\r']
                for x in password_end_indicators:
                    password_end = -1
                    password_end_found = file_content.find(x, password_start)
                    if password_end_found != -1:
                        password_end = password_end_found
                        break
                password = file_content[password_start:password_end]
                break
    return password


print(find_password(cached_files()))
