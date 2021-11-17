
class Storage:

    def __init__(self, hist):
        self.hist = hist
        self.storage = {}

    def count_storage(self):
        for i in range(len(self.hist)):
            if self.hist[i] == 'zakup':
                if not self.storage.get(self.hist[i + 1]):
                    self.storage.update({self.hist[i + 1]: 0})
                self.storage[self.hist[i + 1]] += int(self.hist[i + 3])
            elif self.hist[i] == 'sprzedaz':
                self.storage[self.hist[i + 1]] -= int(self.hist[i + 3])

    def check_item_amount(self, storage_item):
        if not self.storage.get(storage_item):
            return None
        else:
            return self.storage[storage_item]

    def print_storage(self):
        for k, v in self.storage.items():
            print(k, ':', v)

    def print_storage_item(self, storage_item):
        print(storage_item, ':', self.storage.get(storage_item))
