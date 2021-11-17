from functions import check_args
from files import Files
from operations import Operations

args = check_args()

if args:
    if len(args) == 5:
        f = Files(args[1])
        f.read_file()
        o = Operations(f.operations_history)
        o.count_saldo()
        o.saldo -= int(args[3]) * int(args[4])
        if o.saldo >= 0:
            o.add_to_history(args[0], args[2], args[3], args[4])
            f.write_file()
        else:
            print('Za malo srodkow na taki wydatek.\n'
                  'Aby sprawdzic ilosc dostepnych srodkow wybierz '
                  'polecenie: \n'
                  '\t konto.py <nazwa_pliku>')
    else:
        print('Nie podano wszystkich argumentow operacji "zakup". \n'
              '\t zakup.py <nazwa_pliku> <nazwa> <cena> <ilosc> \n'
              'Aby sprawdzic stan magazynu wybierz polecenie: \n'
              '\t magazyn.py <nazwa_pliku> [<nazwa_art1> [<nazwa_art2> [...]]]')
else:
    print('Blad argumentow !!!')
