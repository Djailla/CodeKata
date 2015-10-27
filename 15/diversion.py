import itertools


def get_items(item_size):
    allorderings = itertools.product(['0', '1'], repeat=item_size)

    my_list = []

    for item in allorderings:
        if not '11' in ''.join(item):
            my_list.append(''.join(item))

    print "For %d element, the list size is %d" % (item_size, len(my_list))
    # print '\n'.join(my_list)

for n in [2, 3, 4, 5, 10, 20]:
    get_items(n)
