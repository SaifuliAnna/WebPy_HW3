import abc
import pickle


class CliOutputAbstract(metaclass=abc.ABCMeta):

    def __init__(self, data, f_name):
        self.data = data
        self.__f_name = None
        self.f_name = f_name

    @abc.abstractmethod
    def output_cli(self):
        pass


class CliOutputAddBook(CliOutputAbstract):

    @property
    def f_name(self):
        return self.__f_name

    @f_name.setter
    def f_name(self, f_name):
        parse = f_name.split('.')
        if parse[1] == 'bin':
            self.__f_name = f_name
        else:
            raise ValueError("File must be BIN format")

    def output_cli(self):

        with open(self.__f_name, 'rb') as file:
            unpacked = pickle.load(file)
            print(unpacked)


class CliOutputNote(CliOutputAbstract):

    @property
    def f_name(self):
        return self.__f_name

    @f_name.setter
    def f_name(self, f_name):
        parse = f_name.split('.')
        if parse[1] == 'bin':
            self.__f_name = f_name
        else:
            raise ValueError("File must be BIN format")

    def output_cli(self):

        with open(self.__f_name, 'rb') as file:
            unpacked = pickle.load(file)
            print(unpacked)


if __name__ != '__main__':

    bin_add_book = CliOutputAddBook('AddressBook.bin')
    bin_add_book.output_cli()

    bin_add_note = CliOutputNote('NoteBook.bin')
    bin_add_note.output_cli()
