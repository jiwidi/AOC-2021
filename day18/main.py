import sys

inf = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

ll = [x for x in open(inf).read().strip().split("\n")]


def split(x):
    if x % 2 == 0:
        return [[x // 2], [x // 2]]
    return [[x // 2], [x // 2 + 1]]


def descendr(x):
    while len(x) == 2:
        x = x[1]
    return x


def descendl(x):
    while len(x) == 2:
        x = x[0]
    return x


def reduce_snailfish_a(x, depth, toleft, toright):
    if len(x) == 1:
        return (x, False)
    if depth >= 4:
        if toleft:
            toleft[0] += x[0][0]
        if toright:
            toright[0] += x[1][0]
        return ([0], True)
    n, ok = reduce_snailfish_a(x[0], depth + 1, toleft, descendl(x[1]))
    if ok:
        x[0] = n
        return (x, ok)
    n, ok = reduce_snailfish_a(x[1], depth + 1, descendr(x[0]), toright)
    if ok:
        x[1] = n
        return (x, ok)
    return (x, False)


def reduce_snailfish_b(x, depth, toleft, toright):
    if len(x) == 1:
        if x[0] >= 10:
            return (split(x[0]), True)
        return (x, False)
    n, ok = reduce_snailfish_b(x[0], depth + 1, toleft, descendl(x[1]))
    if ok:
        x[0] = n
        return (x, ok)
    n, ok = reduce_snailfish_b(x[1], depth + 1, descendr(x[0]), toright)
    if ok:
        x[1] = n
        return (x, ok)
    return (x, False)


def reduce_snailfish(x, depth, toleft, toright):
    n, ok = reduce_snailfish_a(x, depth, toleft, toright)
    if ok:
        return n, ok
    return reduce_snailfish_b(x, depth, toleft, toright)


def conv(arr):
    if type(arr) == type([]):
        arr[0] = conv(arr[0])
        arr[1] = conv(arr[1])
        return arr
    return [arr]


def mag(x):
    if len(x) == 1:
        return x[0]
    else:
        return 3 * mag(x[0]) + 2 * mag(x[1])


xx = conv(eval(ll[0]))
for line in ll[1:]:
    l = eval(line)
    l = conv(l)
    xx = [xx, l]
    xx, ok = reduce_snailfish(xx, 0, [], [])
    while ok:
        xx, ok = reduce_snailfish(xx, 0, [], [])
print(mag(xx))

m = []
for a in ll:
    for b in ll:
        xx = [conv(eval(a)), conv(eval(b))]
        xx, ok = reduce_snailfish(xx, 0, [], [])
        while ok:
            xx, ok = reduce_snailfish(xx, 0, [], [])
        m.append(mag(xx))
print(max(m))
