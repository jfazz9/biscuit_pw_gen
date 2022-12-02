'''
    So I'd like it if you could create a pw generator that will output strong pws, i.e.
    with uppercase, lowercase, numbers and symbols...
    But also have a VARIETY of possible biscuits
    Ideally 8-12 characters long but I won't complain if you go crazy'''

from biscuits import all_biscuits, symbols, all_symbols
from random import choice as cho, randint

class Password_gen:
    def __init__(self):
        self.biscuit = cho(all_biscuits) # get biscuit

    def get_symbols(self): # replace symbols in word biscuit
        for a in self.biscuit:
            if a in symbols:
                self.biscuit = self.biscuit.replace(a, symbols[a])
        return self.biscuit

    def adding_uppercase(self): # swap lowercase for upper randomly
        for a in range(len(self.biscuit)//2):
            to_be_caps = randint(0, len(self.biscuit)-1)
            try:
                self.biscuit = self.biscuit.replace(self.biscuit[to_be_caps], self.biscuit[to_be_caps].upper())
            except TypeError:
                continue
        return self.biscuit

    def fill_white_space(self): # using other symbols instead of whitespace
        for a in self.biscuit:
            if a == ' ':
                self.biscuit = self.biscuit.replace(a, cho(all_symbols))
        return self.biscuit

    def adding_numbers(self): # adding numbers depending on length of current password
        number = ''.join([str((randint(0,9))) for a in range(2)])
        if len(self.biscuit) > 10:
            self.biscuit += str(number[0])
        else:
            self.biscuit += str(number)
        return self.biscuit

    def show(self): # display password, rather than calling attribute
        return self.biscuit


if __name__=='__main__':
    new_pass = Password_gen()
    new_pass.get_symbols()
    new_pass.adding_uppercase()
    new_pass.fill_white_space()
    new_pass.adding_numbers()
    print('Here is your new password...')
    print(new_pass.show())
