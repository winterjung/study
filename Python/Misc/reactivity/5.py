class Dep:
    def __init__(self):
        self.subscribers = []

    def depend(self):
        if target and target not in self.subscribers:
            self.subscribers.append(target)

    def notify(self):
        for sub in self.subscribers:
            sub()


class Data:
    def __init__(self, *args, **kwargs):
        for name in kwargs:
            setattr(self, name, kwargs[name])

    def __setattr__(self, name, value):
        if name not in deps:
            deps[name] = Dep()
        result = super().__setattr__(name, value)
        deps[name].notify()
        return result

    def __getattribute__(self, name):
        deps[name].depend()
        value = super().__getattribute__(name)
        return value


deps = {}
data = Data(price=5, quantity=2)
target = None


def watcher(func):
    global target
    target = func
    target()
    target = None


def total_func():
    data.total = data.price * data.quantity

def sale_price_func():
    data.sale_price = data.price * 0.9

watcher(total_func)
watcher(sale_price_func)


if __name__ == '__main__':
    print(f'sale: {data.sale_price:4}, price: {data.price:2}, quantity: {data.quantity}, total: {data.total}')
    data.price = 20
    print(f'sale: {data.sale_price:4}, price: {data.price:2}, quantity: {data.quantity}, total: {data.total}')
    data.quantity = 3
    print(f'sale: {data.sale_price:4}, price: {data.price:2}, quantity: {data.quantity}, total: {data.total}')
