class Dep:
    def __init__(self):
        self.subscribers = []

    def depend(self):
        if target and target not in self.subscribers:
            self.subscribers.append(target)

    def notify(self):
        for sub in self.subscribers:
            sub()


dep = Dep()

price = 5
quantity = 2
total = 0


def target():
    global total
    total = price * quantity


dep.depend()
target()


if __name__ == '__main__':
    print(f'{price}, {quantity}, {total}')
    price = 20
    print(f'{price}, {quantity}, {total}')
    dep.notify()
    print(f'{price}, {quantity}, {total}')
