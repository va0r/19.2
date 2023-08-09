if __name__ == '__main__':
    import os

    try:
        os.system('python3 manage.py loaddata blog_data.json')
        print('BLOG loaded')
    except OSError:
        f'{OSError=}'

    try:
        os.system('python3 manage.py loaddata catalog_data.json')
        print('CATALOG loaded')
    except OSError:
        f'{OSError=}'
