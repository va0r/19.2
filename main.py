if __name__ == '__main__':
    import os

    try:
        os.system('python3 manage.py runserver')
    except OSError:
        f'{OSError=}'
