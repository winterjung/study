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
target = None


def target_func():
    global total
    total = price * quantity


def watcher(func):
    global target
    target = func
    dep.depend()
    target()
    target = None


watcher(target_func)


if __name__ == '__main__':
    print(f'{price}, {quantity}, {total}')
    price = 20
    print(f'{price}, {quantity}, {total}')
    dep.notify()
    print(f'{price}, {quantity}, {total}')
