# -*-coding:utf-8
def dec(func):
    print 'call dec'

    def in_dec(*arg):
        print ('in dec arg=', arg)
        print ('arc len = ', len(arg))
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)
    return in_dec


@dec
def my_sum(*arg, **kw):  # my_sum=in_dec
    print ('in my_sum', arg)
    return sum(arg)


def my_average(*arg, **kw):
    print ('my_average', arg)
    return float(sum(arg)) / len(arg)

print my_sum(1, 2, 3)
