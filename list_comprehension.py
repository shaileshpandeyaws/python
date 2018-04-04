def myfunc(*args):
    return [x for x in args if x%2==0]

print('lis is {}'.format(myfunc(1,2,3,4,5,6,7,8,9,10)))


def myfunc(*args):
    return [x if x%2==0 else 'odd' for x in args ]

print('list comp is {}'.format(myfunc(1,2,3,4,5,6,7,8,9,10)))




lis is [2, 4, 6, 8, 10]
list comp is ['odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd', 10]