def Bisection_Method(left, right, a, Vp, Vf):
    eps = 10 ** -8
    while right - left > eps:
        middle = (right + left) / 2
        #print('mid', middle)
        if derivative(middle, a, Vp, Vf) < 0:
            left = middle
        else:
            right = middle

    return middle

def derivative(x, a, Vp, Vf):
    eps = 10 ** -8
    #print('deriv', (func(x + eps, a, Vp, Vf) - func(x, a, Vp, Vf)) / eps)
    return (func(x + eps, a, Vp, Vf) - func(x, a, Vp, Vf)) / eps

def func(x, a, Vp, Vf):

    length_p = ((0 - x) ** 2 + (1 - a) ** 2) ** 0.5
    length_f = ((x - 1) ** 2 + (a - 0) ** 2) ** 0.5

    func = length_p / Vp + length_f / Vf

    return func

Vp, Vf = [int(x) for x in input().split()]
a_Y = float(input())

print('%.7f' % Bisection_Method(0, 1, a_Y, Vp, Vf))


