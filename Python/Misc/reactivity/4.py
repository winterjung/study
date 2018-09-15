class Data:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def __setattr__(self, name, value):
        print('SET', name, value)
        return super().__setattr__(name, value)

    def __getattribute__(self, name):
        value = super().__getattribute__(name)
        print('GET', name, value)
        return value


data = Data(price=5, quantity=2)

if __name__ == '__main__':
    total = data.price * data.quantity
    data.price = 20
