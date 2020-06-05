def womens_age(n):
    new_age = 20
    base = None
    if n % 2 == 0:
        base = int(n / 2)
    else:
        new_age = 21
        base = int(n / 2)

    return "{}? That's just {}, in base {}!".format(n,new_age,base)
