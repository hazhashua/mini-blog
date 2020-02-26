"""操作数据的类"""


def test_args(a, b=[]):
    a=6
    b.append(5)
    print(a, "    ", id(b), b)


def test_args_n(a, b=None):
    if b==None:
        b = []
    a = 6
    b.append(5)
    print(a, "    ", id(b), b)


def test_args_n1(a, b=5):
    a = 6
    b += 6
    print(a, "    ", id(b), b)


if __name__=="__main__":
    """ 可变对象作为python默认参数 """
    """
    test_args(1,[4])
    test_args(5)
    # test_args(4,[])
    test_args(9)
    test_args(1)
    """
    """
    test_args_n(1,[4])
    test_args_n(5)
    # test_args(4,[])
    test_args_n(9)
    test_args_n(1)
    """
    test_args_n1(1,3)
    test_args_n1(1)
    test_args_n1(2)

    