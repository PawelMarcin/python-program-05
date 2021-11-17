
class Operations:

    def __init__(self, hist):
        self.hist = hist
        self.saldo = 0

    def count_saldo(self):
        for i in range(len(self.hist)):
            if self.hist[i] == 'saldo':
                self.saldo += int(self.hist[i + 1])
            elif self.hist[i] == 'zakup':
                self.saldo -= int(self.hist[i + 2]) * int(self.hist[i + 3])
            elif self.hist[i] == 'sprzedaz':
                self.saldo += int(self.hist[i + 2]) * int(self.hist[i + 3])

    def add_to_history(self, arg0, arg1, arg2, arg3=None):
        if arg0 in ['saldo', 'zakup', 'sprzedaz']:
            self.hist += [arg0, arg1, arg2]
        if arg0 in ['zakup', 'sprzedaz']:
            self.hist += [arg3]

    def print_history(self):
        for i in self.hist:
            print(i)

    def print_saldo(self):
        print(self.saldo)
