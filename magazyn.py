from functions import check_args
from files import Files
from storage import Storage

args = check_args()

if args:
    f = Files(args[1])
    f.read_file()
    s = Storage(f.operations_history)
    s.count_storage()
    if len(args) == 2:
        s.print_storage()
    else:
        for item in args[2:]:
            s.print_storage_item(item)
else:
    print('Blad argumentow !!!')
