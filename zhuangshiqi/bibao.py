# -*-coding:utf-8
def my_sum(*args, **kw):
    if len(args) == 0:
        return 0
    for val in args:
        if not isinstance(val, int):
            return 0
    return sum(args)


def my_sum_1(*arg, **kw):
    print ('in my_sum_1', arg)
    return sum(arg)


def my_average(*args, **kw):
    if len(args) == 0:
        return 0
    for val in args:
        if not isinstance(val, int):
            return 0
    return sum(args) / len(args)


def my_average_1(*arg, **kw):
    return float(sum(arg)) / len(arg)


def dec(func):
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

print (my_sum(1, 2, 3, 4, 5))
print (my_average(1, 2, 3, 4, 5))

my_sum_1 = dec(my_sum_1)
# dec return in_dec -> my_sum_1
# my_sum_1 = in_dec(*arg)


print (my_sum_1(1, 2, 3, 4, 5, 6))
print (my_sum_1(1, 2, 3, 4, 5, '6'))
my_average_x = dec(my_average_1)
print (my_average_x(1, 2, 3, 4, 5, 6))
