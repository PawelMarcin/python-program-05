from functions import check_args
from files import Files
from operations import Operations
from storage import Storage

args = check_args()

if args:
    if len(args) == 5:
        f = Files(args[1])
        f.read_file()
        o = Operations(f.operations_history)
        s = Storage(f.operations_history)
        s.count_storage()
        item_amount = s.check_item_amount(args[2])
        if not item_amount:
            item_amount = 0
        if item_amount >= int(args[4]):
            o.add_to_history(args[0], args[2], args[3], args[4])
            f.write_file()
        else:
            print('Brak na stanie wystarczajacej ilosci artykulu.\n'
                  'Aby sprawdzic dostepna ilosc wybierz '
                  'polecenie: \n'
                  '\t magazyn.py <nazwa_pliku> <nazwa_art>')
    else:
        print('Nie podano wszystkich argumentow operacji "sprzedaz". \n'
              '\t sprzedaz.py <nazwa_pliku> <nazwa> <cena> <ilosc> \n'
              'Aby sprawdzic stan magazynu wybierz polecenie: \n'
              '\t magazyn.py <nazwa_pliku> [<nazwa_art1> [<nazwa_art2> [...]]]')
else:
    print('Blad argumentow !!!')
