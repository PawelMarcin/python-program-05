
class Files:

    def __init__(self, read_path, write_path=None):
        self.read_path = read_path
        if not write_path:
            self.write_path = self.read_path
        else:
            self.write_path = write_path
        self.operations_history = []

    def read_file(self):
        with open(self.read_path, 'r') as file:
            for line in file:
                line = line.rstrip()
                if line != 'stop':
                    self.operations_history.append(line)
                else:
                    break

    def write_file(self):
        with open(self.write_path, 'w') as file:
            for line in self.operations_history:
                file.write(line + '\n')
            file.write('stop')
