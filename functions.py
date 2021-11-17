import sys


def check_args():
    if sys.argv[0] == 'saldo.py':
        if len(sys.argv) in [2, 4]:
            return [sys.argv[0][0: -3]] + sys.argv[1:]
        else:
            return False
    elif sys.argv[0] in ['zakup.py', 'sprzedaz.py']:
        if len(sys.argv) in [2, 5]:
            return [sys.argv[0][0: -3]] + sys.argv[1:]
        else:
            return False
    elif sys.argv[0] in ['konto.py', 'przeglad.py']:
        if len(sys.argv) == 2:
            return [sys.argv[0][0: -3]] + sys.argv[1:]
        else:
            return False
    elif sys.argv[0] == 'magazyn.py':
        if len(sys.argv) >= 2:
            return [sys.argv[0][0: -3]] + sys.argv[1:]
        else:
            return False
