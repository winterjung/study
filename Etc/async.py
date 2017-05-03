import asyncio


@asyncio.coroutine
def A():
    print("난 에러를 낼거야")
    raise Exception("A에서 무슨 문제가 있대")


@asyncio.coroutine
def B():
    print("A에서 갖고올거야")
    a = yield from A()
    print("A에서 갖고왔거 1을 더할거야")
    yield a + 1


@asyncio.coroutine
def C():
    try:
        print("B에서 갖고올거야")
        b = yield from B()
        print("B에서 갖고왔고 얘가 뭐냐면")
        print(b)
    except Exception as e:
        print("C 에서 예외가 발생했어 :", e)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(C())


if __name__ == '__main__':
    main()

# 결과
#
# B에서 갖고올거야
# A에서 갖고올거야
# 난 에러를 낼거야
# C 에서 예외가 발생했어 : A에서 무슨 문제가 있대
