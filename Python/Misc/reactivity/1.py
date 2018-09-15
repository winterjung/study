storage = []


def record():
    storage.append(target)


def replay():
    for run in storage:
        run()


price = 5
quantity = 2
total = 0
target = None


def target_func():
    global total
    total = price * quantity


target = target_func

record()
target()


if __name__ == '__main__':
    print(f'{price}, {quantity}, {total}')
    price = 20
    print(f'{price}, {quantity}, {total}')
    replay()
    print(f'{price}, {quantity}, {total}')
