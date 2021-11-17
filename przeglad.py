from functions import check_args
from files import Files
from operations import Operations

args = check_args()

if args:
    f = Files(args[1])
    f.read_file()
    o = Operations(f.operations_history)
    o.print_history()
else:
    print('Blad argumentow !!!')
