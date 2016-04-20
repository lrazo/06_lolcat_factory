import os
import subprocess
import cat_service


def main():
    print_header()

    folder = get_or_create_output_folder()
    print('Found or created folder {}'.format(folder))
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('-----------------------------------------------')
    print('                 CAT FACTORY')
    print('-----------------------------------------------')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.abspath(os.path.join(base_folder, folder))

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path, )

    return full_path


def download_cats(folder):
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)

    print('Done.')


def display_cats(folder):
    from sys import platform as _platform

    print('Displaying cats in OS Window')
    if _platform == "linux" or _platform == "linux2":
        # linux
        subprocess.call(['xdg-open', folder])
    elif _platform == "darwin":
        # MAC OS X
        subprocess.call(['open', folder])
    elif _platform == "win32" or _platform == "Windows":
        # windows
        subprocess.call(['explorer', folder])
    else:
        print("We don't support you os: " + _platform)


if __name__ == '__main__':
    main()
