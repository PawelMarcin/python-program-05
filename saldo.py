from functions import check_args
from files import Files
from operations import Operations

args = check_args()

if args:
    if len(args) == 4:
        f = Files(args[1])
        f.read_file()
        o = Operations(f.operations_history)
        o.count_saldo()
        o.saldo += int(args[2])
        if o.saldo >= 0:
            o.add_to_history(args[0], args[2], args[3])
            f.write_file()
        else:
            print('Za malo srodkow na taki wydatek.\n'
                  'Aby sprawdzic ilosc dostepnych srodkow wybierz '
                  'polecenie: \n'
                  '\t konto.py <nazwa_pliku>')
    else:
        print('Nie podano wszystkich argumentow operacji "saldo". \n'
              '\t saldo.py <nazwa_pliku> <kwota> <opis transakcji> \n'
              'Aby sprawdzic historie operacji wybierz polecenie: \n'
              '\t przeglad.py <nazwa_pliku>')
else:
    print('Blad argumentow !!!')
