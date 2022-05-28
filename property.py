class Goods:
    def __init__(self, price: int):
        self.__price = price

    @property
    def price(self):
        print('price getter')
        return self.__price

    @price.setter
    def price(self, val: int):
        print('price setter')
        self.__price = val

    @price.deleter
    def price(self):
        print('price deleter')


p = Goods(1)
print(p.price)
p.price = 5

del p.price
