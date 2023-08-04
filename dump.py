if __name__ == '__main__':
    import os

    try:
        os.system('python3 manage.py dumpdata blog > blog_data.json')
        print('BLOG dumped')
    except OSError:
        f'{OSError=}'

    try:
        os.system('python3 manage.py dumpdata catalog > catalog_data.json')
        print('CATALOG dumped')
    except OSError:
        f'{OSError=}'
