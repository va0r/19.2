if __name__ == '__main__':
    import os

    try:
        os.system('python3 manage.py makemigrations')
    except OSError:
        f'{OSError=}'

    try:
        os.system('python3 manage.py migrate')
    except OSError:
        f'{OSError=}'
